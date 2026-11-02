# SPDX-License-Identifier: GPL-3.0-or-later
"""LZ11 + MSBT helpers for 3DS message files."""
import struct

def lz11_decompress(d):
    assert d[0] == 0x11
    size = d[1] | d[2] << 8 | d[3] << 16
    i = 4
    if size == 0:
        size = struct.unpack_from('<I', d, 4)[0]; i = 8
    out = bytearray()
    while len(out) < size:
        flags = d[i]; i += 1
        for bit in range(8):
            if len(out) >= size: break
            if flags & (0x80 >> bit):
                b1 = d[i]; ind = b1 >> 4
                if ind == 0:
                    b2, b3 = d[i+1], d[i+2]; i += 3
                    ln = ((b1 & 0xF) << 4 | b2 >> 4) + 0x11
                    disp = ((b2 & 0xF) << 8 | b3) + 1
                elif ind == 1:
                    b2, b3, b4 = d[i+1], d[i+2], d[i+3]; i += 4
                    ln = ((b1 & 0xF) << 12 | b2 << 4 | b3 >> 4) + 0x111
                    disp = ((b3 & 0xF) << 8 | b4) + 1
                else:
                    b2 = d[i+1]; i += 2
                    ln = ind + 1
                    disp = ((b1 & 0xF) << 8 | b2) + 1
                for _ in range(ln):
                    out.append(out[-disp])
            else:
                out.append(d[i]); i += 1
    return bytes(out)

def lz11_compress(src):
    n = len(src)
    out = bytearray([0x11, n & 0xFF, n >> 8 & 0xFF, n >> 16 & 0xFF])
    assert n < 1 << 24
    table = {}
    pos = 0
    while pos < n:
        flag_idx = len(out); out.append(0); flags = 0
        for bit in range(8):
            if pos >= n: break
            best_len, best_disp = 0, 0
            if pos + 3 <= n:
                key = src[pos:pos+3]
                for cand in reversed(table.get(key, [])[-64:]):
                    disp = pos - cand
                    if disp > 0x1000: break
                    ln = 3
                    mx = min(0x10110, n - pos)
                    while ln < mx and src[cand + ln] == src[pos + ln]:
                        ln += 1
                    if ln > best_len:
                        best_len, best_disp = ln, disp
                        if ln == mx: break
            if best_len >= 3:
                flags |= 0x80 >> bit
                dd = best_disp - 1
                if best_len <= 0x10:
                    out += bytes([(best_len - 1) << 4 | dd >> 8, dd & 0xFF])
                elif best_len <= 0x110:
                    l = best_len - 0x11
                    out += bytes([l >> 4, (l & 0xF) << 4 | dd >> 8, dd & 0xFF])
                else:
                    l = best_len - 0x111
                    out += bytes([0x10 | l >> 12, l >> 4 & 0xFF, (l & 0xF) << 4 | dd >> 8, dd & 0xFF])
                step = best_len
            else:
                out.append(src[pos]); step = 1
            for k in range(pos, pos + step):
                if k + 3 <= n:
                    table.setdefault(src[k:k+3], []).append(k)
            pos += step
        out[flag_idx] = flags
    while len(out) % 4: out.append(0)
    return bytes(out)

def _sections(m):
    assert m[:8] == b'MsgStdBn' and m[8:10] == b'\xff\xfe', 'only little-endian MSBT'
    count = struct.unpack_from('<H', m, 0xE)[0]
    off = 0x20; secs = []
    for _ in range(count):
        magic = m[off:off+4]; size = struct.unpack_from('<I', m, off+4)[0]
        secs.append((magic, off, size))
        off = (off + 0x10 + size + 0xF) & ~0xF
    return secs

def msbt_read(m):
    """Returns (labels_by_index, strings) where strings are raw UTF-16LE byte strings without terminator."""
    secs = {s[0]: s for s in _sections(m)}
    _, toff, _ = secs[b'TXT2']; base = toff + 0x10
    cnt = struct.unpack_from('<I', m, base)[0]
    offs = list(struct.unpack_from('<%dI' % cnt, m, base + 4))
    strings = []
    for o in offs:
        p = base + o; s = bytearray()
        while True:
            c = struct.unpack_from('<H', m, p)[0]
            if c == 0: break
            if c == 0x0E:
                grp, typ, psz = struct.unpack_from('<3H', m, p + 2)
                s += m[p:p+8+psz]; p += 8 + psz; continue
            if c == 0x0F:
                s += m[p:p+6]; p += 6; continue
            s += m[p:p+2]; p += 2
        strings.append(bytes(s))
    labels = {}
    if b'LBL1' in secs:
        _, loff, _ = secs[b'LBL1']; lb = loff + 0x10
        slots = struct.unpack_from('<I', m, lb)[0]
        for k in range(slots):
            n, o = struct.unpack_from('<2I', m, lb + 4 + 8 * k)
            p = lb + o
            for _ in range(n):
                ln = m[p]; name = m[p+1:p+1+ln].decode('ascii'); idx = struct.unpack_from('<I', m, p+1+ln)[0]
                labels[idx] = name; p += 1 + ln + 4
    return labels, strings

def msbt_write(m, new_strings):
    secs = _sections(m)
    out = bytearray(m[:0x20])
    for magic, off, size in secs:
        if magic == b'TXT2':
            cnt = len(new_strings)
            body = bytearray(struct.pack('<I', cnt)); table_end = 4 + 4 * cnt
            offs = []; blob = bytearray()
            for s in new_strings:
                offs.append(table_end + len(blob)); blob += s + b'\x00\x00'
            for o in offs: body += struct.pack('<I', o)
            body += blob
            hdr = bytearray(m[off:off+0x10]); struct.pack_into('<I', hdr, 4, len(body))
            sec = hdr + body
        else:
            sec = bytearray(m[off:off+0x10+size])
        while len(sec) % 0x10: sec.append(0xAB)
        out += sec
    struct.pack_into('<I', out, 0x12, len(out))
    return bytes(out)

def to_display(s):
    """Raw string -> readable text with control codes as {{hex}} tokens."""
    out = []; p = 0
    while p < len(s):
        c = struct.unpack_from('<H', s, p)[0]
        if c == 0x0E:
            psz = struct.unpack_from('<H', s, p + 6)[0]
            out.append('{{' + s[p:p+8+psz].hex() + '}}'); p += 8 + psz
        elif c == 0x0F:
            out.append('{{' + s[p:p+6].hex() + '}}'); p += 6
        else:
            out.append(chr(c)); p += 2
    return ''.join(out)

def from_display(t):
    out = bytearray(); i = 0
    while i < len(t):
        if t.startswith('{{', i):
            j = t.index('}}', i); out += bytes.fromhex(t[i+2:j]); i = j + 2
        else:
            out += struct.pack('<H', ord(t[i])); i += 1
    return bytes(out)
