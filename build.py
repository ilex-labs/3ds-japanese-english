#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Build English LayeredFS files for a Japanese-region 3DS.

Usage:
    python3 build.py dumps [--out out]
    python3 build.py dumps/*.app [--out out]

Pass the folder made by gm9/scripts/dump_system_apps.gm9, or the decrypted
.app files you dumped from your own console with GodMode9. The script
identifies each one from its header, translates the HOME Menu and System
Settings text, validates every string, and writes a ready-to-copy folder:

    out/luma/titles/0004003000008202/romfs/...   (HOME Menu)
    out/luma/titles/0004001000020000/romfs/...   (System Settings)

Copy out/luma onto the root of your SD card, merging with the existing
luma folder.
"""
import argparse
import hashlib
import os
import re
import sys
import unicodedata

from tools import darc, msgtool as M
from tools.inputs import app_paths, error_text, scrub
from tools.ncch import Ncch, NcchError
from translations import (home_menu_1, home_menu_2, home_menu_3, home_menu_4, status_bar,
                          system_settings_1, system_settings_2, system_settings_3,
                          system_settings_4, system_settings_5, system_settings_6)

VERSION = '1.1'

HOME_MENU_TID = 0x0004003000008202
SYSTEM_SETTINGS_TID = 0x0004001000020000
NOTIFICATIONS_TID = 0x0004003000008E02

# Fingerprints of the message tables the translation was made against:
# (number of strings, sha1 of their internal labels). A different system
# version could reorder strings, so the build stops instead of guessing.
EXPECTED = {
    'home_menu': (589, 'fed6edb76563fa47'),
    'status_bar': (59, '65f7a5c59157e6f6'),
    'system_settings': (1309, '0903fb2ff7a587ce'),
}

TOKEN = re.compile(r'\{\{[0-9a-f]+\}\}')
FMT = re.compile(r'%[0-9]*l?[a-zA-Z]')
SIZE_OPEN = re.compile(r'\{\{0e00010000000200[0-9a-f]{2}00\}\}')
SIZE_CLOSE = '{{0f0001000000}}'
JAPANESE = re.compile(r'[\u3040-\u30fa\u30fc-\u30ff\u4e00-\u9fff\uff66-\uff9f]')


class BuildError(Exception):
    pass


def merge(*modules):
    out = {}
    for mod in modules:
        dup = set(out) & set(mod.T)
        if dup:
            raise BuildError(f'duplicate string numbers in {mod.__name__}: {sorted(dup)}')
        out.update(mod.T)
    return out


def width(line):
    w = 0
    for c in line:
        if 0xE000 <= ord(c) <= 0xF8FF or unicodedata.east_asian_width(c) in 'WF':
            w += 2
        else:
            w += 1
    return w


class LongLine:
    """A translated line wider than the Japanese it replaces: it may wrap on screen.
    Not a problem, so these are listed in out/long-lines.txt rather than shown."""
    APPS = {'home_menu': 'HOME Menu', 'system_settings': 'System Settings', 'status_bar': 'Status bar'}

    def __init__(self, table, index, text, width, jp_width):
        self.table, self.index, self.text = table, index, text
        self.width, self.jp_width = width, jp_width

    def describe(self):
        text = ''.join('[button]' if 0xE000 <= ord(c) <= 0xF8FF else c for c in self.text)  # 3DS icon glyphs
        text = ' / '.join(l for l in text.split('\n') if l.strip())
        return f'  [{self.index}] "{text}" ({self.width} characters wide; the Japanese was {self.jp_width})'


def write_long_lines(path, lines):
    """Write the list of lines that may wrap, grouped by app, for people to read."""
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(f'3ds-jpn-english v{VERSION}\n\n'
                f'These {len(lines)} lines are a little longer than the Japanese they replace, so\n'
                f'the 3DS might show them on two lines. That\'s normal and usually looks fine.\n'
                f'If one looks cut off or messy on your console, please open an issue on\n'
                f'GitHub with a photo.\n')
        for table in sorted({l.table for l in lines}, key=lambda t: list(LongLine.APPS).index(t)
                            if t in LongLine.APPS else 99):
            f.write(f'\n{LongLine.APPS.get(table, table)}\n')
            f.write(''.join(l.describe() + '\n' for l in lines if l.table == table))


def validate(name, rows, T, allow_size_codes):
    """Return (errors, warnings) for a table of {'i','label','jp'} rows."""
    errors, warnings = [], []
    for k in T:
        if not 0 <= k < len(rows):
            errors.append(f'{name}#{k}: no such string')
    for r in rows:
        i, jp = r['i'], r['jp']
        if i not in T:
            continue
        en = T[i]
        tag = f"{name}#{i} {r['label']}"

        def norm(s):
            toks = TOKEN.findall(s)
            other = sorted(t for t in toks if not SIZE_OPEN.match(t) and t != SIZE_CLOSE)
            return other, sum(1 for t in toks if SIZE_OPEN.match(t)), toks.count(SIZE_CLOSE)

        jo, jopen, jclose = norm(jp)
        eo, eopen, eclose = norm(en)
        if jo != eo:
            errors.append(f'{tag}: formatting codes differ from the original')
        if eopen - eclose != jopen - jclose:
            errors.append(f'{tag}: font-size codes unbalanced')
        if not allow_size_codes and eopen > jopen:
            errors.append(f'{tag}: added font-size code (renders blank in this app)')
        icons = lambda s: sorted(c for c in s if 0xE000 <= ord(c) <= 0xF8FF)
        if icons(jp) != icons(en):
            errors.append(f'{tag}: button icons differ from the original')
        if sorted(FMT.findall(jp)) != sorted(FMT.findall(en)):
            errors.append(f'{tag}: placeholders differ {FMT.findall(jp)} vs {FMT.findall(en)}')
        if re.search(r'%(?![0-9]*l?[a-zA-Z])', TOKEN.sub('', en)):
            errors.append(f'{tag}: stray % sign (use the full-width \uff05 for a literal percent)')
        if JAPANESE.search(TOKEN.sub('', en)):
            warnings.append(f'{tag}: still contains Japanese')
        jw = max(width(l) for l in TOKEN.sub('', jp).split('\n')) if jp else 0
        ew = max(width(l) for l in TOKEN.sub('', en).split('\n')) if en else 0
        if jw and ew > jw + 2:
            warnings.append(LongLine(name, i, TOKEN.sub('', en), ew, jw))
    return errors, warnings


class Builder:
    def __init__(self, out_dir):
        self.out = out_dir
        self.errors = []
        self.warnings = []
        self.pending = []  # (path, bytes); written only if the whole build passes

    def check_version(self, key, m):
        labels, strs = M.msbt_read(m)
        joined = '\n'.join(labels.get(i, '') for i in range(len(strs)))
        got = (len(strs), hashlib.sha1(joined.encode()).hexdigest()[:16])
        if got != EXPECTED[key]:
            raise BuildError(f'{key}: your system version lays out this text differently than the one '
                             f'the translation was made for (yours: {got[0]} strings, fingerprint {got[1]}; '
                             f'expected: {EXPECTED[key][0]} strings, {EXPECTED[key][1]}). '
                             f'Not building it, to avoid putting text in the wrong places.')

    def translate(self, key, m, T, allow_size_codes):
        self.check_version(key, m)
        labels, strs = M.msbt_read(m)
        rows = [{'i': i, 'label': labels.get(i, ''), 'jp': M.to_display(s)} for i, s in enumerate(strs)]
        e, w = validate(key, rows, T, allow_size_codes)
        self.errors += e
        self.warnings += w
        new = [M.from_display(T.get(r['i'], r['jp'])) for r in rows]
        out = M.msbt_write(m, new)
        if M.msbt_read(out)[1] != new:
            raise BuildError(f'{key}: output does not re-read cleanly')
        done = sum(1 for r in rows if r['jp'] and r['i'] in T)
        total = sum(1 for r in rows if r['jp'])
        print(f'  {key}: {done}/{total} strings translated')
        return out

    def write(self, tid, rel, data):
        comp = M.lz11_compress(data)
        if M.lz11_decompress(comp) != data:
            raise BuildError(f'{rel}: compression round-trip failed')
        dst = os.path.join(self.out, 'luma', 'titles', f'{tid:016X}', 'romfs', *rel.split('/'))
        self.pending.append((dst, comp))
        return dst

    def flush(self):
        for dst, comp in self.pending:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with open(dst, 'wb') as f:
                f.write(comp)

    def status_bar(self, hud_jp):
        return self.translate('status_bar', hud_jp, status_bar.T, allow_size_codes=False)

    def home_menu(self, romfs):
        print('HOME Menu (0004003000008202)')
        hud = self.status_bar(M.lz11_decompress(romfs['message_hud/JP_Japanese/hud_msbt_LZ.bin']))
        menu = self.translate('home_menu', M.lz11_decompress(romfs['message/JP_Japanese/menu_msbt_LZ.bin']),
                              merge(home_menu_1, home_menu_2, home_menu_3, home_menu_4), allow_size_codes=True)
        return [self.write(HOME_MENU_TID, 'message_hud/JP_Japanese/hud_msbt_LZ.bin', hud),
                self.write(HOME_MENU_TID, 'message/JP_Japanese/menu_msbt_LZ.bin', menu)]

    def system_settings(self, romfs):
        print('System Settings (0004001000020000)')
        arc = M.lz11_decompress(romfs['message_JP_LZ.bin'])
        files = darc.files(arc)
        hud = self.status_bar(files['/./message_hud/JP_Japanese/hud.msbt'])
        mset = self.translate('system_settings', files['/./message_mset/JP_Japanese/mset.msbt'],
                              merge(system_settings_1, system_settings_2, system_settings_3,
                                    system_settings_4, system_settings_5, system_settings_6),
                              allow_size_codes=False)
        new_arc = darc.rebuild(arc, {'/./message_hud/JP_Japanese/hud.msbt': hud,
                                     '/./message_mset/JP_Japanese/mset.msbt': mset})
        return [self.write(SYSTEM_SETTINGS_TID, 'message_JP_LZ.bin', new_arc)]


def main():
    # Some Windows consoles can't show every character; never crash on that.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors='replace')
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('apps', nargs='+', help='dumps folder, or decrypted .app files dumped with GodMode9')
    ap.add_argument('--out', default='out', help='output folder (default: out)')
    args = ap.parse_args()

    print(f'3ds-jpn-english v{VERSION}\n')
    b = Builder(args.out)
    written, seen = [], set()
    try:
        for path, label in app_paths(args.apps):
            try:
                with open(path, 'rb') as f:
                    n = Ncch(f.read())
            except (OSError, NcchError) as e:
                print(f'{label}: skipped ({error_text(e)})')
                continue
            tid = n.title_id
            romfs = n.romfs_files() if tid in (HOME_MENU_TID, SYSTEM_SETTINGS_TID) else {}
            if tid == HOME_MENU_TID and 'message/JP_Japanese/menu_msbt_LZ.bin' in romfs:
                written += b.home_menu(romfs)
                seen.add(tid)
            elif tid == SYSTEM_SETTINGS_TID and 'message_JP_LZ.bin' in romfs:
                written += b.system_settings(romfs)
                seen.add(tid)
            elif tid == SYSTEM_SETTINGS_TID:
                print(f'{label}: System Settings manual content, skipped (the main one is the larger .app)')
            elif tid == NOTIFICATIONS_TID:
                print(f'{label}: Notifications is not supported (Luma halts the console on launch; see README)')
            else:
                print(f'{label}: {tid:016X} {n.product_code}'.rstrip() + ' is not a supported Japanese system title, skipped')
    except BuildError as e:
        print(f'\nERROR: {scrub(str(e))}')
        return 1

    width = [w for w in b.warnings if isinstance(w, LongLine)]
    for w in b.warnings:
        if not isinstance(w, LongLine):
            print(f'  warning: {w}')
    if b.errors:
        for e in b.errors:
            print(f'  ERROR: {e}')
        print(f'\n{len(b.errors)} errors. Nothing was written.')
        return 1
    if not written:
        print('\nNothing built. Pass your dumps folder, or the decrypted HOME Menu and/or System Settings .app files.')
        return 1

    b.flush()
    out = scrub(args.out)
    report = os.path.join(args.out, 'long-lines.txt')
    if width:
        write_long_lines(report, width)
    elif os.path.exists(report):
        os.remove(report)  # left over from an earlier build

    print(f'\nBuilt {len(written)} files with 0 errors.')
    if width:
        print(f'{len(width)} lines are a little longer than the Japanese and may show on two lines. '
              f'That\'s normal; they\'re listed in {os.path.join(out, "long-lines.txt")}.')
    print(f'\nCopy the folders inside {os.path.join(out, "luma", "titles")} into luma{os.sep}titles on your SD card:')
    for p in written:
        print(f'  {scrub(p)}')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print('\nStopped.')
        sys.exit(130)
    except Exception:  # unexpected: show the details, but not the user's home folder
        import traceback
        print('\nUnexpected error. If you report it, include everything below.\n')
        print(scrub(traceback.format_exc()))
        sys.exit(1)
