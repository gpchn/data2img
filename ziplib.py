# 用 zstd 格式压缩数据
def zstd_compress(data: bytes) -> bytes:
    from pyzstd import compress

    return compress(data)


# 用 zstd 格式解压数据
def zstd_decompress(data: bytes) -> bytes:
    from pyzstd import decompress

    return decompress(data)
