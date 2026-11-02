# SPDX-License-Identifier: GPL-3.0-or-later
#
# Python port of the LayeredFS symbol search in Luma3DS's loader
# (sysmodules/loader/source/patcher.c, findLayeredFsSymbols), used to
# predict whether Luma can redirect an app's RomFS before you put files
# on the SD card. Luma3DS is (c) Aurora Wright, TuxSH and contributors,
# licensed under GPLv3: https://github.com/LumaTeam/Luma3DS
"""Check whether Luma3DS LayeredFS can patch a title.

Usage:
    python3 -m tools.lfs_check dumps/*.app

Luma must find five FS functions in the app's code. If any is missing,
Luma's loader halts the console (svcBreak) when the app starts while a
luma/titles/<id>/romfs folder exists for it. The Japanese Notifications
applet (0004003000008E02) is one such title: fsMountArchive is missing.
"""
import struct
import sys

from .ncch import Ncch, NcchError

FUNCS = ('fsMountArchive', 'fsUnMountArchive', 'fsRegisterArchive', 'fsTryOpenFile', 'fsOpenFileDirectly')


def _u32(c, a):
    return struct.unpack_from('<I', c, a)[0]


def _func_start(c, pos):
    while pos >= 4:
        pos -= 4
        if struct.unpack_from('<H', c, pos + 2)[0] == 0xE92D:  # push {...}
            return pos
    return None


def find_symbols(code, size):
    found = {}
    for addr in range(0, size - 3, 4):
        w = _u32(code, addr)
        key = None
        if w == 0xE5970010 and 'fsMountArchive' not in found and addr + 12 <= size \
                and _u32(code, addr + 4) == 0xE1CD20D8 and (_u32(code, addr + 8) & 0xFFFFFF) == 0x008D0000:
            key = 'fsMountArchive'
        elif w == 0xE24DD028 and 'fsMountArchive' not in found and addr + 16 <= size \
                and _u32(code, addr + 4) == 0xE1A04000 and _u32(code, addr + 8) == 0xE59F60A8 \
                and _u32(code, addr + 12) == 0xE3A0C001:
            key = 'fsMountArchive'
        elif w == 0xE2844001 and 'fsUnMountArchive' not in found and addr + 12 <= size \
                and _u32(code, addr + 4) == 0xE3540020 and _u32(code, addr + 8) == 0x3AFFFFF0:
            key = 'fsUnMountArchive'
        elif w == 0xE353003A and 'fsUnMountArchive' not in found and addr + 12 <= size \
                and (_u32(code, addr + 4) & 0xFFFFFF0F) == 0x0A000009 \
                and (_u32(code, addr + 8) & 0xFFFF0FF0) == 0xE1A00400:
            key = 'fsUnMountArchive'
        elif w == 0xE3500008 and 'fsRegisterArchive' not in found and addr + 12 <= size \
                and (_u32(code, addr + 4) & 0xFFF00FF0) == 0xE1800400 \
                and (_u32(code, addr + 8) & 0xFFF00FF0) == 0xE1800FC0:
            key = 'fsRegisterArchive'
        elif w == 0xE351003A and 'fsTryOpenFile' not in found and addr + 0x40 <= size \
                and _u32(code, addr + 4) == 0x1AFFFFFC and _u32(code, addr + 0x34) == 0xE590C000 \
                and _u32(code, addr + 0x3C) == 0xE12FFF3C:
            key = 'fsTryOpenFile'
        elif w == 0x08030204 and 'fsOpenFileDirectly' not in found:
            key = 'fsOpenFileDirectly'
        if key:
            f = _func_start(code, addr)
            if f is not None:
                found[key] = f
    return found


def check(ncch):
    text_size, _, _ = ncch.code_layout()
    found = find_symbols(ncch.code(), text_size)
    return {name: found.get(name) for name in FUNCS}


def main(paths):
    ok_all = True
    for path in paths:
        try:
            n = Ncch(open(path, 'rb').read())
        except (OSError, NcchError) as e:
            print(f'{path}: {e}')
            ok_all = False
            continue
        res = check(n)
        missing = [k for k, v in res.items() if v is None]
        verdict = 'OK - LayeredFS should work' if not missing else 'NOT SUPPORTED - Luma will halt on launch'
        print(f'{path}: {n.title_id:016X} {n.product_code}: {verdict}')
        for k, v in res.items():
            print(f'    {k:20s} {"0x%06x" % v if v is not None else "missing"}')
        ok_all &= not missing
    return 0 if ok_all else 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
