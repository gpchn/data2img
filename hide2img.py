#!/usr/bin/env python3
# coding=utf-8

from pathlib import Path


def main() -> None:
    from argparse import ArgumentParser
    from base64 import b64decode
    from math import sqrt, ceil
    from io import BytesIO

    # 解析命令行参数
    parser = ArgumentParser(description="将数据隐藏到图片中，或从图片中还原数据")

    # 选择输入方式
    parser_input = parser.add_mutually_exclusive_group(required=True)
    parser_input.add_argument(
        "-e", "--encode", type=Path, help="以 文件的二进制数据 作为原始数据"
    )
    parser_input.add_argument(
        "-t", "--encode-text", help="以 UTF-8 编码后的文本 作为原始数据"
    )
    parser_input.add_argument(
        "-d", "--decode", type=Path, help="以 文件图片文件 作为原图片数据"
    )
    parser_input.add_argument(
        "-u", "--decode-uri", help="以 以 Data URI scheme 作为原图片数据"
    )
    parser_input.add_argument(
        "-D", "--decode2", type=Path, help="以 文件图片文件 作为含隐藏信息图片数据"
    )
    parser_input.add_argument(
        "-U", "--decode-uri2", help="以 以 Data URI scheme 作为含隐藏信息图片数据"
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

    if args.encode or args.encode_text:
        if args.encode:
            data = args.encode.read_bytes()
        elif args.encode_text:
            data = args.encode_text.encode("utf-8")

        side_len = ceil(sqrt(len(data) / 3))

    elif args.decode or args.decode_uri:
        if args.decode:
            img1 = args.decode
        elif args.decode_uri:
            img1 = args.decode_uri

        if args.decode2:
            img2 = args.decode2
        elif args.decode_uri2:
            img2 = args.decode_uri2

        decode_img(img1, img2, args.output)
    else:
        print("请指定输入方式，使用 -h 查看帮助")
        return


# 将数据隐藏到图片中
def create_img(data: list[int], side_len: int, output: Path | None, show: bool) -> None:
    from PIL import Image, ImageDraw
    from base64 import b64encode
    from io import BytesIO
    from tqdm import tqdm

    ...


# 从图片还原数据
def decode_img(img_path1: Path, img_path2: Path, output: Path):
    from PIL import Image
    from tqdm import tqdm

    img1 = Image.open(img_path1)
    img2 = Image.open(img_path2)
    ...


if __name__ == "__main__":
    main()
