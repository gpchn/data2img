# DATA 2 IMG

English (en-US) | [Simplified Chinese (zh-CN)](README.zh-CN.md)

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

A Python script for encoding data into images.

This is a tool that uses Python to encode arbitrary data into PNG images or decode data back from PNG images. The script utilizes the Zstandard compression algorithm to improve data compression ratios.

This repository contains the following:

1. [data2img.py script](data2img.py): A script for encoding data into images or decoding data back from images.
2. [code.png](code.png): A PNG image of the code.
3. [demo.mp4](demo.mp4): A demonstration video.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Dependencies](#dependencies)
- [Usage Instructions](#usage-instructions)
  - [Encode](#encode)
  - [Decode](#decode)
  - [Print](#print)
- [Examples](#examples)
- [Related Repositories](#related-repositories)
- [Maintainers](#maintainers)
- [How to Contribute](#how-to-contribute)
- [License](#license)

## Dependencies

This project runs on [Python 3](https://www.python.org/). Please ensure you have Python 3 and the following dependencies installed locally:

- [Pillow](https://pypi.org/project/Pillow/) (for handling images)
- [pyzstd](https://pypi.org/project/pyzstd/) (for compressing and decompressing data)
- [tqdm](https://pypi.org/project/tqdm/) (for displaying progress bars)

You can install these dependencies using the following command:

```sh
$ pip install Pillow pyzstd tqdm
```

## Usage Instructions

```
usage: data2img.py [-h] (-e ENCODE | -t ENCODE_TEXT | -d DECODE | -u DECODE_URI) [-p | -o OUTPUT] [-s]

将数据编码成图片，或将图片解码成数据

options:
  -h, --help            show this help message and exit
  -e ENCODE, --encode ENCODE
                        以 文件的二进制数据 作为原始数据
  -t ENCODE_TEXT, --encode-text ENCODE_TEXT
                        以 utf-8 编码后的文本 作为原始数据
  -d DECODE, --decode DECODE
                        以 本地图片文件 作为图片数据
  -u DECODE_URI, --decode-uri DECODE_URI
                        以 Data URI scheme 作为图片数据
  -p, --print           将结果直接打印到终端（UTF-8 解码后的文本 / Base64 字符串 / Data URI scheme）        
  -o OUTPUT, --output OUTPUT
                        指定输出文件
  -s, --show            存储后打开图像文件（仅在 encode 模式下生效）
```

### Encode

Encode data into an image, where the data source can be a file or text.
Encoding from a file into an image:

```bash
python data2img.py -e <file_path> [-o <output_image_file_path>] [-s]
```

Encoding from text into an image:

```bash
python data2img.py -t <text> [-o <output_image_file_path>] [-s]
```

If no output file path is specified, it defaults to out.png in the current directory.

If the -s parameter is used, the image file will automatically open upon completion of encoding.

### Decode

Decode an image back into data.

Decoding from a local image file:

```bash
python data2img.py -d <image_file_path> [-o <output_data_file_path>]
```

Decoding from a Data URI scheme:

```bash
python data2img.py -u <Data_URI_scheme> [-o <output_data_file_path>]
```

If no output file path is specified, it defaults to a .out file with the same name as the input file.

### Print

Print the result directly to the terminal.

Printing the encoded Data URI scheme:

```bash
python data2img.py -e <file_path> -p
```

Printing the decoded data:

```bash
python data2img.py -d <image_file_path> -p
```

If the decoded data is text, it will attempt to print it in UTF-8 encoding. If this fails, it will print the Base64 encoded string.

## Examples

Please refer to the [following video](demo.mp4).

![demo video](demo.mp4)

## Related Repositories

- [hide2img](https://github.com/gpchn/hide2img): A tool for hiding data within images.

## Maintainers

[@gpchn](https://github.com/gpchn)

## How to Contribute

Your contributions are very welcome! [Open an Issue](https://github.com/gpchn/data2img/issues/new) or submit a Pull Request.

<!--### Contributors
Thank you to the following people who have participated in the project:
<a href="graphs/contributors"><img src="https://opencollective.com/standard-readme/contributors.svg?width=890&button=false" /></a>-->

## License

[Apache 2.0](LICENSE) © gpchn

```
Copyright 2025 gpchn
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```