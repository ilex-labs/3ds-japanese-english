# SPDX-License-Identifier: GPL-3.0-or-later
"""Command-line input and output helpers shared by build.py and lfs_check.

app_paths() turns arguments into .app files. Each argument can be a file, a
wildcard such as dumps/*.app (expanded here, because Windows shells pass it
through unchanged), or a folder. Folders are searched recursively, so the
folder written by gm9/scripts/dump_system_apps.gm9 (one subfolder per title
ID) can be passed as it is. Unfinished copies left by an interrupted dump
end in .app.part and are not picked up.

Output never shows full paths: people paste it into bug reports, and a full
path usually contains their user name. Files are labelled relative to the
folder that was passed (0004001000020000/0000004d.app), and scrub() hides
the home folder in anything else that might hold a path.
"""
import glob
import os


def app_paths(args):
    """Return [(path, label)] for every .app file the arguments name."""
    out = []
    for p in args:
        if os.path.isdir(p):
            found = []
            for root, dirs, files in os.walk(p):
                dirs.sort()
                # ._name files are macOS metadata left on FAT SD cards, not dumps
                found += [os.path.join(root, f) for f in sorted(files)
                          if f.lower().endswith('.app') and not f.startswith('._')]
            if not found:
                print(f'{folder_name(p)}: no .app files in this folder')
            out += [(f, os.path.relpath(f, p)) for f in found]
        elif glob.has_magic(p):
            out += [(f, os.path.basename(f)) for f in sorted(glob.glob(p))
                    if not os.path.basename(f).startswith('._')] or [(p, os.path.basename(p))]
        else:
            out.append((p, os.path.basename(p)))
    return out


def folder_name(p):
    return os.path.basename(os.path.normpath(p)) or p


def error_text(e):
    """An exception's message without the file path OSError adds."""
    if isinstance(e, OSError) and e.strerror:
        return e.strerror
    return scrub(str(e))


def scrub(text):
    """Replace the user's home folder with ~ wherever it appears."""
    homes = {os.path.expanduser('~')}
    try:
        homes.add(os.path.realpath(os.path.expanduser('~')))
    except OSError:
        pass
    for home in sorted((h for h in homes if h and h != '~'), key=len, reverse=True):
        variants = {home, home.replace('\\', '/'), home.replace('\\', '\\\\')}
        for v in variants:
            text = _replace_path(text, v, '~', ignore_case=os.name == 'nt')
    return text


def _replace_path(text, old, new, ignore_case):
    """Replace old where it is a whole path prefix (not C:\\Users\\bob in C:\\Users\\bobby)."""
    hay, needle = (text.lower(), old.lower()) if ignore_case else (text, old)
    out, i = [], 0
    while True:
        j = hay.find(needle, i)
        if j < 0:
            return ''.join(out) + text[i:]
        end = j + len(old)
        if end < len(text) and (text[end].isalnum() or text[end] in '_-.'):
            out.append(text[i:end])  # part of a longer name: keep it
        else:
            out += [text[i:j], new]
        i = end
