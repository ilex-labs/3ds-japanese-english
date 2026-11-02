# SPDX-License-Identifier: GPL-3.0-or-later
"""Minimal DARC (3DS archive) reader/rebuilder that preserves layout."""
import struct

def read(d):
    assert d[:4] == b'darc' and d[4:6] == b'\xff\xfe'
    hsize, ver, fsize, toff, tlen, doff = struct.unpack_from('<HIIIII', d, 6)
    root_size = struct.unpack_from('<I', d, toff + 8)[0]
    n = root_size
    ents = [struct.unpack_from('<III', d, toff + 12 * i) for i in range(n)]
    names_off = toff + 12 * n
    def name(o):
        p = names_off + o; s = bytearray()
        while d[p:p+2] != b'\0\0': s += d[p:p+2]; p += 2
        return s.decode('utf-16le')
    out = []  # (index, path, is_dir, offset, size)
    stack = []
    for i, (no, a, b) in enumerate(ents):
        is_dir = bool(no & 0x01000000)
        nm = name(no & 0x00FFFFFF)
        while stack and i >= stack[-1][1]:
            stack.pop()
        path = '/'.join([s[0] for s in stack] + [nm]) if nm else ''
        out.append((i, path, is_dir, a, b))
        if is_dir:
            stack.append((nm, b))
    return {'hdr': (hsize, ver, toff, tlen, doff), 'ents': ents, 'list': out}

def files(d):
    info = read(d)
    return {p: d[a:a+b] for i, p, isdir, a, b in info['list'] if not isdir}

def rebuild(d, replacements):
    """Replace file contents by path; keeps entry order and data alignment."""
    info = read(d)
    hsize, ver, toff, tlen, doff = info['hdr']
    file_ents = [(i, p, a, b) for i, p, isdir, a, b in info['list'] if not isdir]
    # alignment: largest power of two dividing every original data offset (cap 0x80)
    align = 0x80
    while align > 4 and any(a % align for _, _, a, _ in file_ents):
        align //= 2
    out = bytearray(d[:doff])
    ents = list(info['ents'])
    order = sorted(file_ents, key=lambda e: e[2])  # original data order
    first = True
    for i, p, a, b in order:
        data = replacements.get(p, d[a:a+b])
        if not first:
            while len(out) % align: out.append(0)
        first = False
        no, _, _ = ents[i]
        ents[i] = (no, len(out), len(data))
        out += data
    for i, e in enumerate(ents):
        struct.pack_into('<III', out, toff + 12 * i, *e)
    struct.pack_into('<I', out, 0xC, len(out))
    return bytes(out)
