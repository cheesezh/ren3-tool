# !/usr/bin/env python
# encoding: utf-8

"""
@Author  : hezhang
@Email   : hezhang@mobvoi.com
@Time    : 2019/10/26 上午8:48
@File    : cut.py
@IDE     : PyCharm
"""

import config
from PIL import Image
import time
import os


def cut_fun(left, upper, right, lower, name):
    cropped = copyIm.crop((left, upper, right, lower))
    print("正在截取排名信息...[ {}.jpg ]".format(name))
    cropped.save("tmp"+os.path.sep+"{}.jpg".format(name))

for file in config.FILES:
    upper_step = config.SMALL_IMAGE_STEP
    rank_left = 158 + config.RANK_OFFSET
    upper = config.UPPER_BOUNDRY
    rank_right = rank_left + 47
    lower = upper + config.SMALL_IMAGE_HEIGHT

    name_left = rank_right + 55 + config.NAME_OFFSET
    name_right = name_left + 150

    score_left = name_right + 25 + config.SCORE_OFFSET
    score_right = score_left + 100

    print("准备裁剪图片...[ {} ]".format(file))
    suffix_idx = file.rfind(".")
    image_name = file[0:suffix_idx]
    img = Image.open(file)
    (width, height) = img.size
    white_img = Image.new('RGB', (config.COVER_1_WIDTH, height), (170, 193, 224))
    white_img_2 = Image.new('RGB', (config.COVER_2_WIDTH, height), (170, 193, 224))
    copyIm = img.copy()
    copyIm.paste(white_img, (rank_left + 42 + config.COVER_1_OFFSET, 0))
    copyIm.paste(white_img_2, (name_right + config.COVER_2_OFFSET, 0))

    if os.path.exists(config.COVERED_PICTURE):
        os.remove(config.COVERED_PICTURE)
    copyIm.save(config.COVERED_PICTURE)

    time_list = []
    while lower < height:
        t = int(time.time())
        time_list.append(t)
        info_name = "info_{}".format(t)
        cut_fun(rank_left, upper, score_right, lower, info_name)
        upper += upper_step
        lower = upper + config.SMALL_IMAGE_HEIGHT
        # break
        time.sleep(1)

print("\n下一步请执行命令：python 1-tencent-ocr.py")