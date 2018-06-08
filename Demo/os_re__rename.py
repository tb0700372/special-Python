#!/usr/bin/env python
# -*- coding: UTF-8 -*
# 截图图片重命名

import os
import re

image_lists = []
old_image = []


def Snip():
    """Snip截图重命名,命名规则为按照软件命名规则,把图片重命名为1-N"""
    # 遍历当前目录所有文件
    for root, dirs, files in os.walk(os.getcwd()):

        # 取出文件名和路径
        for file in files:
            if file[-3:] == 'png':
                old_image.append(os.path.join(root, file))  # 取出路径
                # 文件编号处理
                new_image = re.sub(r'^.*?_([0-9]*?)\..*?$', '\\1', file)
                image_lists.append(int(new_image))  # 编号

    # 文件名排序
    image_lists.sort()

    # 开始处理文件名ls
    i = 0
    while i < len(image_lists):
        for p in old_image:
            if p.find("_" + str(image_lists[i]) + ".png") > 0:
                os.rename(p, os.path.join(os.getcwd(), str(i) + ".png"))  # 重命名
                break

        i += 1

if __name__ == '__main__':
    Snip()
