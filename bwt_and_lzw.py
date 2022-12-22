from bwt import bw_restore, bw_transform
from lzw import compress, decompress


def bwt_plus_lzw_compress(message):
    id, msg = bw_transform(message)
    compressed = compress(msg)
    return id, compressed


def bwt_plus_lzw_decompress(id, compressed):
    decompressed = decompress(compressed)
    return bw_restore(id, decompressed)


if __name__ == "__main__":
    id, compressed = bwt_plus_lzw_compress("TOBEORNOTTOBEORTOBEORNOT")
    print(id, compressed)
    decompressed = bwt_plus_lzw_decompress(id, compressed)
    print(decompressed)