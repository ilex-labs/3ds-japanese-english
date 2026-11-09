# SPDX-License-Identifier: GPL-3.0-or-later
"""Read and write the .bmsm text files of the updated StreetPass Mii Plaza.

Layout (worked out from the files; every file in the update re-writes to
identical bytes):
  u32 entry count, u32 field count (always 6), then for each entry:
    label, style        ASCII, NUL-terminated, zero-padded to a multiple of 4
    text                FF FE, then UTF-16LE text and a NUL, zero-padded to
                        a multiple of 8 (counted from after the FF FE)
    three more fields   ASCII, as above
  then any trailing bytes, kept as they are.

Text uses \\r\\n line breaks; read() and write() leave them alone.
"""
import struct


class BmsmError(Exception):
    pass


def _ascii(b, p):
    q = b.find(b'\x00', p)
    if q < 0:
        raise BmsmError(f'unterminated field at 0x{p:x}')
    n = q - p + 1
    return b[p:q].decode('latin-1'), p + n + (-n % 4)


def _text(b, p):
    if b[p:p + 2] != b'\xff\xfe':
        raise BmsmError(f'text field without FF FE at 0x{p:x}')
    s = q = p + 2
    while b[q:q + 2] != b'\x00\x00':
        if q >= len(b):
            raise BmsmError(f'unterminated text at 0x{p:x}')
        q += 2
    n = q - s + 2
    return b[s:q].decode('utf-16le'), s + n + (-n % 8)


def read(b):
    """Return ([[label, style, text, f1, f2, f3], ...], trailing bytes)."""
    if len(b) < 8:
        raise BmsmError('file too short')
    count, nfields = struct.unpack_from('<II', b, 0)
    if nfields != 6:
        raise BmsmError(f'expected 6 fields per entry, found {nfields}')
    p, entries = 8, []
    for _ in range(count):
        label, p = _ascii(b, p)
        style, p = _ascii(b, p)
        text, p = _text(b, p)
        f1, p = _ascii(b, p)
        f2, p = _ascii(b, p)
        f3, p = _ascii(b, p)
        entries.append([label, style, text, f1, f2, f3])
    return entries, b[p:]


def _a(s):
    raw = s.encode('latin-1') + b'\x00'
    return raw + b'\x00' * (-len(raw) % 4)


def write(entries, tail=b''):
    out = bytearray(struct.pack('<II', len(entries), 6))
    for label, style, text, f1, f2, f3 in entries:
        raw = text.encode('utf-16le') + b'\x00\x00'
        out += _a(label) + _a(style) + b'\xff\xfe' + raw + b'\x00' * (-len(raw) % 8) + _a(f1) + _a(f2) + _a(f3)
    return bytes(out) + tail
