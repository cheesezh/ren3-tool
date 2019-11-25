# !/usr/bin/env python
# encoding: utf-8

"""
@Author  : hezhang
@Email   : hezhang@mobvoi.com
@Time    : 2019/10/26 上午8:48
@File    : cut.py
@IDE     : PyCharm
"""

import shenyuan_config as config
from PIL import Image
import time
import os


def cut_fun(left, upper, right, lower, name):
    cropped = copyIm.crop((left, upper, right, lower))  # (left, upper, right, lower)
    white_img_3 = Image.new('RGB', (config.COVER_3_WIDTH, config.COVER_3_HEIGHT), (170, 193, 224))
    cropped.paste(white_img_3, (config.COVER_3_OFFSET, config.COVER_3_START_TOP + config.COVER_3_STEP * 0))
    cropped.paste(white_img_3, (config.COVER_3_OFFSET, config.COVER_3_START_TOP + config.COVER_3_STEP * 1))
    cropped.paste(white_img_3, (config.COVER_3_OFFSET, config.COVER_3_START_TOP + config.COVER_3_STEP * 2))
    cropped.paste(white_img_3, (config.COVER_3_OFFSET, config.COVER_3_START_TOP + config.COVER_3_STEP * 3))
    cropped.paste(white_img_3, (config.COVER_3_OFFSET, config.COVER_3_START_TOP + config.COVER_3_STEP * 4))
    cropped.paste(white_img_3, (config.COVER_3_OFFSET, config.COVER_3_START_TOP + config.COVER_3_STEP * 5))

    print("正在截取排名信息[ {} ]".format(name))
    cropped.save("tmp"+os.path.sep+"{}.jpg".format(name))

for tmp_file in config.FILES:

    HEIGHT = config.SMALL_IMAGE_HEIGHT
    upper_step = config.SMALL_IMAGE_STEP
    rank_left = 475 + config.RANK_OFFSET
    upper = config.START_TOP
    rank_right = rank_left + 47
    lower = upper + HEIGHT

    name_left = rank_right + 55 + config.NAME_OFFSET
    name_right = name_left + 150


    print("准备裁剪图片[ {} ]".format(tmp_file))
    suffix_idx = config.FILE_NAME.rfind(".")
    image_name = config.FILE_NAME[0:suffix_idx]
    img = Image.open(tmp_file)
    (width, height) = img.size
    white_img = Image.new('RGB', (config.COVER_1_WIDTH, height), (170, 193, 224))

    copyIm = img.copy()
    copyIm.paste(white_img, (config.COVER_1_OFFSET, 0))

    if os.path.exists(config.COVERED_PICTURE):
        os.remove(config.COVERED_PICTURE)
    copyIm.save(config.COVERED_PICTURE)


    time_list = []
    while lower < height:
        t = int(time.time())
        time_list.append(t)
        info_name = "info_{}".format(t)
        cut_fun(rank_left, upper, name_right, lower, info_name)
        upper += upper_step
        lower = upper + HEIGHT
        time.sleep(1)