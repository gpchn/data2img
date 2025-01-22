#!/usr/bin/env python3
# coding=utf-8

from pathlib import Path


def main() -> None:
    from argparse import ArgumentParser
    from base64 import b64decode
    from math import sqrt, ceil
    from io import BytesIO

    # 解析命令行参数
    parser = ArgumentParser(description="将数据隐藏在图片中，或将从图片中提取数据")

    # 选择输入方式
    parser_input = parser.add_mutually_exclusive_group(required=True)
    parser_input.add_argument(
        "-e", "--encode", type=Path, help="以 文件的二进制数据 作为原始数据"
    )
    parser_input.add_argument(
        "-t", "--encode-text", help="以 utf-8 编码后的文本 作为原始数据"
    )
    parser_input.add_argument(
        "-d", "--decode", type=Path, help="以 本地图片文件 作为图片数据"
    )
    parser_input.add_argument(
        "-u", "--decode-uri", help="以 Data URI scheme 作为图片数据"
    )

    # 选择输出方式
    parser_output = parser.add_mutually_exclusive_group(required=False)
    parser_output.add_argument(
        "-p",
        "--print",
        action="store_true",
        help="将结果直接打印到终端（UTF-8 解码后的文本 / Base64 字符串 / Data URI scheme）",
    )
    parser_output.add_argument("-o", "--output", type=Path, help="指定输出文件")

    # 是否在存储后打开图像文件
    parser.add_argument(
        "-s",
        "--show",
        default=False,
        action="store_true",
        help="存储后打开图像文件（仅在 encode 模式下生效）",
    )

    args = parser.parse_args()

    # 数据来源：文本 / 文件
    # 文本编码：utf-8 / ascii
    if args.encode_text:
        data = args.encode_text.encode("utf-8")
    elif args.encode:
        data = args.encode.read_bytes()

    elif args.decode_uri:
        # 将 Data URI scheme 转换为虚拟文件
        img_buffer = BytesIO(b64decode(args.decode_uri.split(",")[1]))
        if args.print:
            output = False
        else:
            output = args.output if args.output else Path(f"{args.decode}.out")
        decode_img(img_buffer, output)
        return
        # decode 完全由 decode_img() 完成，到此为止
    elif args.decode:
        if args.print:
            output = False
        else:
            output = args.output if args.output else Path(f"{args.decode}.out")
        decode_img(args.decode, output)
        return
        # decode 完全由 decode_img() 完成，到此为止
    else:
        print("请指定输入方式，使用 -h 查看帮助")
        return

    print("已经读取数据，正在处理中……")

    # 压缩数据
    data = zstd_compress(data)
    print("数据压缩完成，正在转换为像素……")
    # 将 bytes 转换成 list[int]，在末尾加一个 225
    data_int_list = [data_int for data_int in data] + [225]
    # 获取数据长度
    data_length = len(data_int_list)
    print(
        f"数据长度：{data_length - 1} Bytes"
    )  # 减 1 是因为最后一个 225 不算在数据长度内
    # 取平方根，向上取整
    side_len = ceil(sqrt(data_length / 3))
    print(f"图片尺寸：{side_len}x{side_len}")
    # 填充数组至最近的平方数（图片是正方形）
    data_int_list += [0] * (side_len**2 * 3 - data_length)
    # 此时 data_length ** 2 == data_length

    print("像素转换完成，正在生成图像……")
    if args.print:
        output = False
    else:
        output = args.output if args.output else Path("./out.png")
    create_img(data_int_list, side_len, output, args.show)


# 将数据转换为图片
def create_img(data: list[int], side_len: int, output: Path | None, show: bool) -> None:
    from PIL import Image, ImageDraw
    from base64 import b64encode
    from io import BytesIO
    from tqdm import tqdm

    # 创建一个 RGB 图像
    img = Image.new(mode="RGB", size=(side_len, side_len))
    draw = ImageDraw.Draw(img)

    # 将数据写入图像
    data_index = 0
    with tqdm(total=side_len**2, desc="正在生成图像", unit="px") as pbar:
        for x in range(side_len):
            for y in range(side_len):
                draw.point(
                    (x, y),
                    (data[data_index], data[data_index + 1], data[data_index + 2]),
                )
                data_index += 3
                pbar.update()

    # 保存图像
    if output:
        img.save(output, format="PNG")
        print(f"图像已保存至 {output.absolute()}")
    else:
        img_buffer = BytesIO()
        img.save(img_buffer, format="PNG")
        print(
            f"data:image/png;base64,{b64encode(img_buffer.getvalue()).decode("utf-8")}"
        )

    if show:
        img.show()


# 从图片还原数据
def decode_img(img_path: Path, output: Path):
    from PIL import Image
    from tqdm import tqdm

    # 读取图像
    img = Image.open(img_path)
    pixels = img.load()
    side_len = img.size[0]
    print(f"图像已打开，大小为 {side_len}x{side_len}")

    # 将像素数据转换为整数列表
    data = []
    with tqdm(total=side_len**2, desc="正在读取数据", unit="px") as pbar:
        for x in range(side_len):
            for y in range(side_len):
                data += pixels[x, y]
                pbar.update()

    # 移除末尾的 255 和填充的 0
    while data[-1] == 0:
        data.pop()
    data.pop()  # 移除最后一个 255

    print(f"数据读取完成，长度为 {len(data)} Bytes，正在解压数据……")

    # 解压
    data = zstd_decompress(bytes(data))

    # 输出
    if output:
        output.write_bytes(data)
        print(f"数据已解压并保存至 {output.absolute()}")
    else:
        try:
            print(data.decode("utf-8"))
        except UnicodeDecodeError:
            print(b64encode(data).decode("utf-8"))


# 用 zstd 格式压缩数据
def zstd_compress(data: bytes) -> bytes:
    from pyzstd import compress

    return compress(data)


# 用 zstd 格式解压数据
def zstd_decompress(data: bytes) -> bytes:
    from pyzstd import decompress

    return decompress(data)


if __name__ == "__main__":
    main()
