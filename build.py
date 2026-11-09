#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Build English LayeredFS files for a Japanese-region 3DS.

Usage:
    python3 build.py dumps [--out out]
    python3 build.py dumps/*.app [--out out]

Pass the folder made by gm9/scripts/dump_system_apps.gm9, or the decrypted
.app files you dumped from your own console with GodMode9. The script
identifies each one from its header, translates the text of the apps it
supports, validates every string, and writes a ready-to-copy folder:

    out/luma/titles/0004003000008202/romfs/...   (HOME Menu)
    out/luma/titles/0004001000020000/romfs/...   (System Settings)
    out/luma/titles/0004001000020700/romfs/...   (Mii Maker)
    out/luma/titles/0004003000008702/romfs/...   (Game Notes)
    out/luma/titles/0004001000020800/romfs/...   (StreetPass Mii Plaza)
    out/luma/titles/0004001000020400/romfs/...   (Nintendo 3DS Camera)
    out/luma/titles/0004001000020500/romfs/...   (Nintendo 3DS Sound)

Copy out/luma onto the root of your SD card, merging with the existing
luma folder.
"""
import argparse
import hashlib
import os
import re
import struct
import sys
import unicodedata

from tools import bmsm, darc, msgarc, msgtool as M
from tools.inputs import app_paths, error_text, scrub
from tools.ncch import Ncch, NcchError
from translations import (camera, home_menu_1, home_menu_2, home_menu_3, home_menu_4, mii_maker,
                          plaza_park, plaza_system, sound, status_bar,
                          system_settings_1, system_settings_2, system_settings_3,
                          system_settings_4, system_settings_5, system_settings_6)

VERSION = '1.2'

HOME_MENU_TID = 0x0004003000008202
SYSTEM_SETTINGS_TID = 0x0004001000020000
MII_MAKER_TID = 0x0004001000020700
GAME_NOTES_TID = 0x0004003000008702
NOTIFICATIONS_TID = 0x0004003000008E02
CAMERA_TID = 0x0004001000020400
SOUND_TID = 0x0004001000020500
# StreetPass Mii Plaza: the text comes from its update (on the SD card), but
# Luma looks for the files under the base app's title ID.
PLAZA_UPDATE_TID = 0x0004000E00020800
PLAZA_BASE_TID = 0x0004001000020800
PLAZA_DIR = 'message/JP_Japanese/message/'

# The file each supported app keeps its text in; an .app without it is the
# app's manual or other content, not the program itself.
MAIN_FILE = {
    HOME_MENU_TID: 'message/JP_Japanese/menu_msbt_LZ.bin',
    SYSTEM_SETTINGS_TID: 'message_JP_LZ.bin',
    MII_MAKER_TID: 'message/JP_Japanese.arc',
    GAME_NOTES_TID: 'lang/JP_Japanese/message.msbt',
    PLAZA_UPDATE_TID: PLAZA_DIR + 'system/system.bmsm',
    CAMERA_TID: 'msg/JP_Japanese.LZ',
    SOUND_TID: 'msg/JP_Japanese.LZ',
}

# Fingerprints of the message tables the translation was made against:
# (number of strings, sha1 of their internal labels). A different system
# version could reorder strings, so the build stops instead of guessing.
EXPECTED = {
    'home_menu': (589, 'fed6edb76563fa47'),
    'status_bar': (59, '65f7a5c59157e6f6'),
    'system_settings': (1309, '0903fb2ff7a587ce'),
    'mii_maker': (268, 'c6139d36900b7e03'),
    'game_notes': (61, '1e55f1b218767db3'),
    'game_notes_english': (61, '1e55f1b218767db3'),
    'camera_main': (169, '45b350b048c201b0'),
    'camera_dialogs': (477, '08bfb2dcda54a799'),
    'camera_guide': (684, '8625a14b00a4ce66'),
    'sound_main': (166, '197fdf0adb8f8782'),
    'sound_dialogs': (335, '2ae922483674b630'),
    'sound_guide': (657, '31057d5481dda5e6'),
}

# StreetPass Mii Plaza: file -> (module, table, number of entries, sha1 of their labels).
# Only the Plaza itself, including the shop rabbit's introduction of each
# game: the games inside it (Puzzle Swap, Find Mii and the ones sold in its
# shop) stay Japanese.
PLAZA_FILES = {
    'system/bg': (plaza_system, 'BG', 32, '88c2b65058d9cd2d'),
    'system/dialogue': (plaza_system, 'DIALOGUE', 5, 'be98af37bad99e8d'),
    'system/system': (plaza_system, 'SYSTEM', 103, 'f011ad4db29cb656'),
    'system/text_sample': (plaza_system, 'TEXT_SAMPLE', 9, '5751dec5eaf6affd'),
    'park/balloon': (plaza_park, 'BALLOON', 70, '84922bfb26ff17ae'),
    'park/birthday': (plaza_park, 'BIRTHDAY', 96, '5bfcafddaae2d1ca'),
    'park/boot': (plaza_system, 'BOOT', 51, '9478c0b7dddbbbb8'),
    'park/card': (plaza_park, 'CARD', 85, 'a55fecd8b7bc9f31'),
    'park/celebrate': (plaza_park, 'CELEBRATE', 210, '07fa411815f8b043'),
    'park/commerce': (plaza_park, 'COMMERCE', 236, '8985871b42d5aaa6'),
    'park/gate': (plaza_park, 'GATE', 196, '185c84fb84eb5469'),
    'park/hat': (plaza_park, 'HAT', 207, '10b25cb84a3cf77b'),
    'park/hat_shop': (plaza_park, 'HAT_SHOP', 17, '5d8d8866590e2a18'),
    'park/introduction': (plaza_park, 'INTRODUCTION', 126, '975fe54c1616da5a'),
    'park/map': (plaza_park, 'MAP', 35, '2add3a1e682f5722'),
    'park/mii_setting': (plaza_park, 'MII_SETTING', 123, 'aae6dcea18c6970e'),
    'park/option': (plaza_park, 'OPTION', 207, '304eb448ad11bded'),
    'park/park': (plaza_park, 'PARK', 316, 'e87dce2e9ae87b79'),
    'park/presen': (plaza_park, 'PRESEN', 778, '886dad663364c60d'),
    'park/prof': (plaza_park, 'PROF', 77, 'caf5e0e1812d7943'),
    'park/sound': (plaza_park, 'SOUND', 379, '84e3b3b911f50b4d'),
    'park/vip_room': (plaza_park, 'VIP_ROOM', 12, '565131e2f9d7d841'),
}
PLAZA_TAG = re.compile(r'\[[^\]\n]*\]')  # [0], [MII_NAME], [System:Color name="red" ] ...

TOKEN = re.compile(r'\{\{[0-9a-f]+\}\}')
FMT = re.compile(r'%[0-9]*l?[a-zA-Z]')
SIZE_OPEN = re.compile(r'\{\{0e00010000000200[0-9a-f]{2}00\}\}')
SIZE_CLOSE = '{{0f0001000000}}'
JAPANESE = re.compile(r'[\u3040-\u30fa\u30fc-\u30ff\u4e00-\u9fff\uff66-\uff9f]')


class BuildError(Exception):
    pass


class VersionMismatch(BuildError):
    """One app's text is laid out differently from the version the table was made for."""


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
    APPS = {'home_menu': 'HOME Menu', 'system_settings': 'System Settings', 'mii_maker': 'Mii Maker',
            'game_notes': 'Game Notes', 'status_bar': 'Status bar', 'plaza': 'StreetPass Mii Plaza',
            'camera_main': 'Nintendo 3DS Camera', 'camera_dialogs': 'Nintendo 3DS Camera',
            'camera_guide': 'Nintendo 3DS Camera (How to Use)', 'sound_main': 'Nintendo 3DS Sound',
            'sound_dialogs': 'Nintendo 3DS Sound', 'sound_guide': 'Nintendo 3DS Sound (How to Use)'}

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


def validate_plaza(name, entries, T):
    """Return (errors, warnings) for one Plaza file; T is keyed by label, text uses \\n."""
    errors, warnings = [], []
    labels = {e[0] for e in entries}
    for k in T:
        if k not in labels:
            errors.append(f'{name} {k}: no such string')
    for e in entries:
        label, jp = e[0], e[2].replace('\r\n', '\n')
        if label not in T:
            continue
        en, tag = T[label], f'{name} {label}'
        if sorted(PLAZA_TAG.findall(jp)) != sorted(PLAZA_TAG.findall(en)):
            errors.append(f'{tag}: placeholders or formatting differ from the original')
        icons = lambda s: sorted(c for c in s if 0xE000 <= ord(c) <= 0xF8FF)
        if icons(jp) != icons(en):
            errors.append(f'{tag}: button icons differ from the original')
        if '\r' in en:
            errors.append(f'{tag}: contains a carriage return (write line breaks as \\n)')
        if JAPANESE.search(PLAZA_TAG.sub('', en)):
            warnings.append(f'{tag}: still contains Japanese')
        jw = max(width(l) for l in PLAZA_TAG.sub('', jp).split('\n'))
        ew = max(width(l) for l in PLAZA_TAG.sub('', en).split('\n'))
        if jw and ew > jw + 2:
            warnings.append(LongLine('plaza', f'{name} {label}', PLAZA_TAG.sub('', en), ew, jw))
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
            raise VersionMismatch(f'{key}: your system version lays out this text differently than the one '
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

    def write(self, tid, rel, data, compress=True):
        comp = M.lz11_compress(data) if compress else data
        if compress and M.lz11_decompress(comp) != data:
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

    def mii_maker(self, romfs):
        print('Mii Maker (0004001000020700)')
        arc = M.lz11_decompress(romfs['message/JP_Japanese.arc'])
        edit = self.translate('mii_maker', darc.files(arc)['/./edit.msbt'], mii_maker.T, allow_size_codes=False)
        new_arc = darc.rebuild(arc, {'/./edit.msbt': edit})
        return [self.write(MII_MAKER_TID, 'message/JP_Japanese.arc', new_arc)]

    def game_notes(self, romfs):
        """Game Notes already has English text (for Taiwan): use it in place of the Japanese."""
        print('Game Notes (0004003000008702)')
        hud = self.status_bar(romfs['lang/JP_Japanese/hud.msbt'])
        english = romfs['lang/TW_English/message.msbt']
        self.check_version('game_notes_english', english)
        labels, strs = M.msbt_read(english)
        by_label = {labels[i]: M.to_display(s) for i, s in enumerate(strs)}
        jp_labels = M.msbt_read(romfs['lang/JP_Japanese/message.msbt'])[0]
        T = {i: by_label[name] for i, name in jp_labels.items() if by_label.get(name)}
        message = self.translate('game_notes', romfs['lang/JP_Japanese/message.msbt'], T, allow_size_codes=False)
        return [self.write(GAME_NOTES_TID, 'lang/JP_Japanese/hud.msbt', hud, compress=False),
                self.write(GAME_NOTES_TID, 'lang/JP_Japanese/message.msbt', message, compress=False)]

    def plaza(self, romfs):
        print('StreetPass Mii Plaza (update 0004000E00020800)')
        done = total = 0
        written = []
        for rel, (mod, table, count, fp) in PLAZA_FILES.items():
            path = PLAZA_DIR + rel + '.bmsm'
            if path not in romfs:
                raise VersionMismatch(f'plaza: {rel}.bmsm is missing from your update. Not building it.')
            try:
                entries, tail = bmsm.read(romfs[path])
            except bmsm.BmsmError as e:
                raise VersionMismatch(f'plaza: {rel}.bmsm could not be read ({e}). Not building it.')
            got = (len(entries), hashlib.sha1('\n'.join(e[0] for e in entries).encode()).hexdigest()[:16])
            if got != (count, fp):
                raise VersionMismatch(f'plaza: your update lays out {rel}.bmsm differently than the one the '
                                      f'translation was made for (yours: {got[0]} strings, fingerprint {got[1]}; '
                                      f'expected: {count} strings, {fp}). Not building it, to avoid putting '
                                      f'text in the wrong places.')
            T = getattr(mod, table)
            e, w = validate_plaza(rel, entries, T)
            self.errors += e
            self.warnings += w
            for ent in entries:
                if JAPANESE.search(ent[2]):
                    total += 1
                    done += ent[0] in T
                if ent[0] in T:
                    ent[2] = T[ent[0]].replace('\n', '\r\n')
            out = bmsm.write(entries, tail)
            if bmsm.read(out)[0] != entries:
                raise BuildError(f'plaza {rel}: output does not re-read cleanly')
            written.append(self.write(PLAZA_BASE_TID, PLAZA_DIR + rel + '.bmsm', out, compress=False))
        print(f'  plaza: {done}/{total} strings translated (the games inside the Plaza are not translated)')
        return written


    def msg_archive(self, tid, key, romfs, files):
        """Camera and Sound keep three .msbt files in msg/JP_Japanese.LZ."""
        try:
            arc = M.lz11_decompress(romfs['msg/JP_Japanese.LZ'])
            inside = msgarc.files(arc)
        except (msgarc.MsgArcError, AssertionError, ValueError, IndexError) as e:
            raise VersionMismatch(f'{key}: msg/JP_Japanese.LZ could not be read ({e}). Not building it.')
        new = {}
        for name, (suffix, T) in files.items():
            if name not in inside:
                raise VersionMismatch(f'{key}: {name} is missing. Not building it.')
            # These apps shrink long button labels with size codes themselves, so translations may too.
            new[name] = self.translate(f'{key}_{suffix}', inside[name], T, allow_size_codes=True)
        return [self.write(tid, 'msg/JP_Japanese.LZ', msgarc.rebuild(arc, new))]

    def camera(self, romfs):
        print('Nintendo 3DS Camera (0004001000020400)')
        return self.msg_archive(CAMERA_TID, 'camera', romfs, {
            'P.msbt': ('main', camera.MAIN), 'P_dlg.msbt': ('dialogs', camera.DIALOGS),
            'P_tips.msbt': ('guide', camera.GUIDE)})

    def sound(self, romfs):
        print('Nintendo 3DS Sound (0004001000020500)')
        return self.msg_archive(SOUND_TID, 'sound', romfs, {
            'S.msbt': ('main', sound.MAIN), 'S_dlg.msbt': ('dialogs', sound.DIALOGS),
            'S_tips.msbt': ('guide', sound.GUIDE)})


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
    written, seen, mismatched = [], set(), []
    try:
        for path, label in app_paths(args.apps):
            try:
                with open(path, 'rb') as f:
                    n = Ncch(f.read())
            except (OSError, NcchError) as e:
                print(f'{label}: skipped ({error_text(e)})')
                continue
            tid = n.title_id
            romfs = {}
            if tid in MAIN_FILE:
                try:
                    romfs = n.romfs_files()
                except (NcchError, struct.error, ValueError):  # unreadable RomFS: treat as not the program
                    romfs = {}
            builders = {HOME_MENU_TID: b.home_menu, SYSTEM_SETTINGS_TID: b.system_settings,
                        MII_MAKER_TID: b.mii_maker, GAME_NOTES_TID: b.game_notes, PLAZA_UPDATE_TID: b.plaza,
                        CAMERA_TID: b.camera, SOUND_TID: b.sound}
            if tid in MAIN_FILE and MAIN_FILE[tid] in romfs:
                if tid in seen:
                    print(f'{label}: {tid:016X} was already built from another file, skipped')
                    continue
                # A version mismatch skips just this app; undo anything it queued.
                mark = len(b.errors), len(b.warnings), len(b.pending)
                try:
                    written += builders[tid](romfs)
                except VersionMismatch as e:
                    del b.errors[mark[0]:], b.warnings[mark[1]:], b.pending[mark[2]:]
                    print(f'  skipped: {scrub(str(e))}')
                    mismatched.append(f'{tid:016X}')
                    continue
                seen.add(tid)
            elif tid in MAIN_FILE:
                print(f'{label}: {tid:016X} manual or other content, skipped (the program is the larger .app)')
            elif tid == PLAZA_BASE_TID:
                print(f'{label}: StreetPass Mii Plaza without its update, skipped (the translation is built from '
                      f'the update, 0004000E00020800; see README)')
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
    mismatch_note = (f'\nSkipped {len(mismatched)} app(s) whose system version differs from the one the '
                     f'translation was made for: {", ".join(mismatched)}. Please open an issue on GitHub and '
                     f'paste the lines starting with "skipped:" above.') if mismatched else ''
    if not written:
        if mismatch_note:
            print(mismatch_note)
        print('\nNothing built. Pass your dumps folder, or the decrypted .app files of the apps listed in the README.')
        return 1

    b.flush()
    out = scrub(args.out)
    report = os.path.join(args.out, 'long-lines.txt')
    if width:
        write_long_lines(report, width)
    elif os.path.exists(report):
        os.remove(report)  # left over from an earlier build

    print(f'\nBuilt {len(written)} files with 0 errors.')
    if mismatch_note:
        print(mismatch_note)
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
