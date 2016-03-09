# coding=utf-8
from PIL import Image
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')     # 输入文件
parser.add_argument('-o', '--output')  # 输出文件
parser.add_argument('--width', type = int, default=80)
parser.add_argument('--height', type = int, default=80)

# 获取参数
args = parser.parse_args()

img = args.file
width = args.width
height = args.height
output = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上


def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':

    im = Image.open(img)
    im = im.resize((width, height), Image.NEAREST)

    txt = ""

    for i in range(height):
        for j in range(width):
            # 获取图片j,i处的r,g, b,alpha值
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    # 字符画输出到文件
    if output:
        with open(output, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)


