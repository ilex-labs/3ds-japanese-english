# SPDX-License-Identifier: GPL-3.0-or-later
"""Read decrypted NCCH content (.app files dumped and decrypted with GodMode9).

Provides the title ID / product code, the RomFS file tree, and the
decompressed ExeFS .code (for the Luma compatibility check).
"""
import struct

MEDIA_UNIT = 0x200
NONE = 0xFFFFFFFF


class NcchError(Exception):
    pass


class Ncch:
    def __init__(self, data):
        if data[0x100:0x104] != b'NCCH':
            raise NcchError('not an NCCH file (expected a .app content file)')
        flags = data[0x188:0x190]
        if not flags[7] & 0x04:
            raise NcchError('file is still encrypted; decrypt it in GodMode9 first '
                            '(A on the file > NCCH image options... > Decrypt file)')
        self.data = data

    @property
    def title_id(self):
        return struct.unpack_from('<Q', self.data, 0x118)[0]

    @property
    def product_code(self):
        return self.data[0x150:0x160].rstrip(b'\0').decode('ascii', 'replace')

    # ---- RomFS -----------------------------------------------------------
    def romfs_files(self):
        """Return {path: bytes} for every file in the RomFS (paths use '/')."""
        off = struct.unpack_from('<I', self.data, 0x1B0)[0] * MEDIA_UNIT
        size = struct.unpack_from('<I', self.data, 0x1B4)[0] * MEDIA_UNIT
        if size == 0:
            return {}
        r = self.data[off:off + size]
        if r[:4] != b'IVFC':
            raise NcchError('RomFS header not found')
        master_hash_size = struct.unpack_from('<I', r, 0x8)[0]
        l3_block = 1 << struct.unpack_from('<I', r, 0x4C)[0]
        l3 = (0x60 + master_hash_size + l3_block - 1) // l3_block * l3_block
        h = struct.unpack_from('<10I', r, l3)
        dir_meta, file_meta, data_off = l3 + h[3], l3 + h[7], l3 + h[9]

        def name_at(o, n):
            return r[o:o + n].decode('utf-16le')

        files = {}

        def walk(doff, path):
            _, _, child, cfile, _, nlen = struct.unpack_from('<6I', r, dir_meta + doff)
            name = name_at(dir_meta + doff + 0x18, nlen)
            here = f'{path}/{name}' if doff else ''
            f = cfile
            while f != NONE:
                _, sib, fo, fsz, _, fn = struct.unpack_from('<IIQQII', r, file_meta + f)
                fname = name_at(file_meta + f + 0x20, fn)
                files[f'{here}/{fname}'.lstrip('/')] = r[data_off + fo:data_off + fo + fsz]
                f = sib
            c = child
            while c != NONE:
                walk(c, here)
                c = struct.unpack_from('<I', r, dir_meta + c + 4)[0]

        walk(0, '')
        return files

    # ---- ExeFS .code -----------------------------------------------------
    def code_layout(self):
        """(text_size, ro_size, data_size) from the extended header."""
        exh = self.data[0x200:0x600]
        text = struct.unpack_from('<III', exh, 0x10)[2]
        ro = struct.unpack_from('<III', exh, 0x20)[2]
        data = struct.unpack_from('<III', exh, 0x30)[2]
        return text, ro, data

    def code(self):
        """Decompressed .code (text + ro + data)."""
        compressed = self.data[0x200 + 0xD] & 1
        exefs = struct.unpack_from('<I', self.data, 0x1A0)[0] * MEDIA_UNIT
        for i in range(10):
            name, off, size = struct.unpack_from('<8sII', self.data, exefs + 16 * i)
            if name.rstrip(b'\0') == b'.code':
                c = self.data[exefs + 0x200 + off:exefs + 0x200 + off + size]
                return blz_decompress(c) if compressed else c
        raise NcchError('no .code in ExeFS')


def blz_decompress(c):
    """3DS backward-LZ decompression used for ExeFS .code."""
    extra = struct.unpack_from('<I', c, len(c) - 4)[0]
    hdr = struct.unpack_from('<I', c, len(c) - 8)[0]
    hdr_len, comp_len = hdr >> 24, hdr & 0xFFFFFF
    out = bytearray(c) + bytearray(extra)
    dst, src, end = len(out), len(c) - hdr_len, len(c) - comp_len
    while src > end:
        src -= 1
        flags = c[src]
        for _ in range(8):
            if src <= end:
                break
            if flags & 0x80:
                src -= 2
                v = c[src] | c[src + 1] << 8
                ln, disp = (v >> 12) + 3, (v & 0xFFF) + 3
                for _ in range(ln):
                    dst -= 1
                    out[dst] = out[dst + disp]
            else:
                src -= 1
                dst -= 1
                out[dst] = c[src]
            flags = (flags << 1) & 0xFF
    return bytes(out)
