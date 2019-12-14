# !/usr/bin/env python
# encoding: utf-8

"""
@Author  : hezhang
@Email   : hezhang@mobvoi.com
@Time    : 2019/10/27 下午7:48
@File    : config.py
@IDE     : PyCharm
"""


FILES = [
    "120601.jpeg",  # 截图的名字, jpg／jpeg／png格式都可以
    "120602.jpeg"
]

#=========下边基本不需要配置==============

from PIL import Image

FILE_NAME = FILES[0]
img = Image.open(FILE_NAME)
(width, height) = img.size

# 自动计算截图宽度
# 晚晚：1000
# 心悦：1500
SNAPSHOT_DEVICE_WIDTH = str(width)

print("截图宽度为：{}".format(SNAPSHOT_DEVICE_WIDTH))

CONFIG = {
    "1000": {
        "COVER_1_OFFSET" : 510,
        "COVER_1_WIDTH" : 48,
        "RANK_OFFSET" : 0,
        "START_TOP" : 60,
        "COVER_3_OFFSET" : 80,
        "SMALL_IMAGE_HEIGHT" : 309,
        "SMALL_IMAGE_STEP" : 462,
        "COVER_3_WIDTH" : 100,
        "COVER_3_HEIGHT" : 22,
        "COVER_3_START_TOP" : 28,
        "COVER_3_STEP" : 52,
        "NAME_OFFSET" : 0

    },
    "1500": {
        "COVER_1_OFFSET" : 823,
        "COVER_1_WIDTH" : 60,
        "RANK_OFFSET" : 283,
        "START_TOP" : 89,
        "SMALL_IMAGE_STEP" : 693,
        "COVER_3_OFFSET" : 120,
        "SMALL_IMAGE_HEIGHT": 468,
        "COVER_3_WIDTH" : 100,
        "COVER_3_HEIGHT" : 33,
        "COVER_3_START_TOP" : 42,
        "COVER_3_STEP" : 78,
        "NAME_OFFSET" : 70
    }
}
# 一些位置相关的配置，因为截图的手机不同，所以可能需要适当调整
COVER_1_OFFSET = CONFIG[SNAPSHOT_DEVICE_WIDTH]["COVER_1_OFFSET"]  # 遮盖区1的偏移量，正数右移／负数左移
COVER_1_WIDTH = CONFIG[SNAPSHOT_DEVICE_WIDTH]["COVER_1_WIDTH"]  # 遮盖区1的偏移量，正数右移／负数左移
RANK_OFFSET = CONFIG[SNAPSHOT_DEVICE_WIDTH]["RANK_OFFSET"]  # 排名左边界的偏移量，正数右移／负数左移
START_TOP = CONFIG[SNAPSHOT_DEVICE_WIDTH]["START_TOP"]
SMALL_IMAGE_HEIGHT = CONFIG[SNAPSHOT_DEVICE_WIDTH]["SMALL_IMAGE_HEIGHT"]
COVER_3_OFFSET = CONFIG[SNAPSHOT_DEVICE_WIDTH]["COVER_3_OFFSET"]  # 遮盖区3的偏移量，正数右移／负数左移
COVER_3_WIDTH = CONFIG[SNAPSHOT_DEVICE_WIDTH]["COVER_3_WIDTH"]
COVER_3_HEIGHT = CONFIG[SNAPSHOT_DEVICE_WIDTH]["COVER_3_HEIGHT"]
NAME_OFFSET = CONFIG[SNAPSHOT_DEVICE_WIDTH]["NAME_OFFSET"]  # 昵称左边界的偏移量，正数右移／负数左移
COVER_3_START_TOP = CONFIG[SNAPSHOT_DEVICE_WIDTH]["COVER_3_START_TOP"]
COVER_3_STEP = CONFIG[SNAPSHOT_DEVICE_WIDTH]["COVER_3_STEP"]
SMALL_IMAGE_STEP = CONFIG[SNAPSHOT_DEVICE_WIDTH]["SMALL_IMAGE_STEP"]
COVERED_PICTURE = 'picture_with_covered_area.jpg'  # 带遮盖区的图片名称

# 固定配置，别修改
ocr_app_id = "2123257550"
ocr_app_key = "fphTgDZTkmZ200xk"
members = "members.txt"  # 当前家族的成员列表，直接从大表中复制出来即可