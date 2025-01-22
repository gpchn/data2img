# DATA 2 IMG

[English (en-US)](README.md) | 简体中文 (zh-CN)

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

一个用于将数据编码为图片的 Python 脚本。

这是一个使用 Python 将任意数据编码为 PNG 图片，或从 PNG 图片解码回数据的工具。该脚本使用了 Zstandard 压缩算法来提高数据压缩比。

本仓库包含以下内容：

1. [data2img.py 脚本](data2img.py)：用于将数据编码为图片或从图片解码回数据的脚本。
2. [code.png](code.png)：代码的 PNG 图片。
3. [demo.mp4](demo.mp4)：演示视频。

## 内容列表

- [内容列表](#内容列表)
- [依赖](#依赖)
- [使用说明](#使用说明)
  - [编码（encode）](#编码encode)
  - [解码（decode）](#解码decode)
  - [打印（print）](#打印print)
- [示例](#示例)
- [相关仓库](#相关仓库)
- [维护者](#维护者)
- [如何贡献](#如何贡献)
- [使用许可](#使用许可)

## 依赖

这个项目使用 [Python 3](https://www.python.org/) 来运行。请确保你本地安装了 Python 3 和以下依赖：

- [Pillow](https://pypi.org/project/Pillow/) (用于处理图片)
- [pyzstd](https://pypi.org/project/pyzstd/)（用于压缩和解压缩数据）
- [tqdm](https://pypi.org/project/tqdm/)（用于显示进度条）

你可以使用以下命令安装这些依赖：

```sh
$ pip install Pillow pyzstd tqdm
```

## 使用说明

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

### 编码（encode）

将数据编码为图片，数据来源可以是文件或文本。

从文件编码为图片：

```bash
python data2img.py -e <文件路径> [-o <输出图片文件路径>] [-s]
```

从文本编码为图片：

```bash
python data2img.py -t <文本> [-o <输出图片文件路径>] [-s]
```

如果不指定输出文件路径，默认输出到当前目录下的 out.png 文件。

如果使用 -s 参数，编码完成后会自动打开图片文件。

### 解码（decode）

将图片解码回数据。

从本地图片文件解码：

```bash
python data2img.py -d <图片文件路径> [-o <输出数据文件路径>]
```

从 Data URI scheme 解码：

```bash
python data2img.py -u <Data URI scheme> [-o <输出数据文件路径>]
```

如果不指定输出文件路径，默认输出到与输入文件同名的 .out 文件。

### 打印（print）

将结果直接打印到终端。

打印编码后的 Data URI scheme：

```bash
python data2img.py -e <文件路径> -p
```

打印解码后的数据：

```bash
python data2img.py -d <图片文件路径> -p
```

如果解码后的数据是文本，则会尝试以 UTF-8 编码打印。如果失败，则打印 Base64 编码后的字符串。

## 示例

请参考 [以下视频](demo.mp4) 。

![demo video](demo.mp4)

## 相关仓库

- [hide2img](https://github.com/gpchn/hide2img)：一个用于将数据隐藏在图片中的工具。

## 维护者

[@gpchn](https://github.com/gpchn)

## 如何贡献

非常欢迎你的加入！[提一个 Issue](https://github.com/gpchn/data2img/issues/new) 或者提交一个 Pull Request。

<!--### 贡献者

感谢以下参与项目的人：
<a href="graphs/contributors"><img src="https://opencollective.com/standard-readme/contributors.svg?width=890&button=false" /></a>-->

## 使用许可

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