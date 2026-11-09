# SPDX-License-Identifier: GPL-3.0-or-later
"""Read and rebuild the small message archives used by Nintendo 3DS Camera and
Nintendo 3DS Sound (msg/JP_Japanese.LZ, LZ11-compressed).

Layout (worked out from the files; both rebuild to identical bytes):
  six 0x40-byte slots: file name (NUL-padded, 0x38 bytes), u32 offset, u32 size;
  unused slots are all zeros. File data follows, each file starting on a
  0x80-byte boundary, and the archive is padded to a multiple of 0x80.
"""
import struct

SLOTS = 6
SLOT = 0x40
ALIGN = 0x80


class MsgArcError(Exception):
    pass


def _entries(arc):
    if len(arc) < SLOTS * SLOT:
        raise MsgArcError('archive too short')
    out = []
    for i in range(SLOTS):
        slot = arc[i * SLOT:(i + 1) * SLOT]
        name = slot[:0x38].rstrip(b'\0')
        if not name:
            if slot.strip(b'\0'):
                raise MsgArcError(f'unexpected data in empty slot {i}')
            continue
        off, size = struct.unpack_from('<II', slot, 0x38)
        if off + size > len(arc):
            raise MsgArcError(f'{name!r} runs past the end of the archive')
        out.append((i, name.decode('ascii'), off, size))
    return out


def files(arc):
    """Return {name: bytes}."""
    return {name: arc[off:off + size] for _, name, off, size in _entries(arc)}


def rebuild(arc, replace):
    """Return the archive with the files in replace ({name: bytes}) swapped in."""
    entries = _entries(arc)
    unknown = set(replace) - {e[1] for e in entries}
    if unknown:
        raise MsgArcError(f'no such files in the archive: {sorted(unknown)}')
    first = min(off for _, _, off, _ in entries)
    head = bytearray(arc[:first])
    data = bytearray()
    for i, name, off, size in sorted(entries, key=lambda e: e[2]):  # keep the original file order
        blob = replace.get(name, arc[off:off + size])
        pos = first + len(data)
        struct.pack_into('<II', head, i * SLOT + 0x38, pos, len(blob))
        data += blob + b'\0' * (-len(blob) % ALIGN)
    return bytes(head + data)
