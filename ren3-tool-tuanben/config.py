# !/usr/bin/env python
# encoding: utf-8

"""
@Author  : hezhang
@Email   : hezhang@mobvoi.com
@Time    : 2019/10/27 下午7:48
@File    : config.py
@IDE     : PyCharm
"""

FILES = [  # 截图的名字, jpg／jpeg／png格式都可以
    "1214hetun01.jpeg",
    "1214hetun02.jpeg"
]

# 小寒/心悦 截图，黑边是否在右边？
BLACK_ON_RIGHT = False  # True or False


#=========下边配置不需要更改==============

from PIL import Image

FILE_NAME = FILES[0]
img = Image.open(FILE_NAME)
(width, height) = img.size

# 自动计算截图宽度
# 晚晚：1000
# 心悦：1500
SNAPSHOT_DEVICE_WIDTH = str(width)


FILE_NAME = FILES[0]

CONFIG = {
    "1500": {
        "COVER_1_OFFSET": 0,
        "COVER_1_WIDTH": 50,
        "COVER_2_OFFSET": -1,
        "COVER_2_WIDTH": 25,
        "RANK_OFFSET": 0,  # 左边黑
        # "RANK_OFFSET": -52,  # 右边黑
        "NAME_OFFSET": 0,
        "UPPER_BOUNDRY": 220,
        "SMALL_IMAGE_HEIGHT": 410,
        "SMALL_IMAGE_STEP": 693,
        "SCORE_OFFSET": 0
    },
    "1000" : {
        "COVER_1_OFFSET": -15,
        "COVER_1_WIDTH": 34,
        "COVER_2_OFFSET": -86,
        "COVER_2_WIDTH": 17,
        "UPPER_BOUNDRY": 148,
        "RANK_OFFSET": -67,
        "NAME_OFFSET": 0,
        "SMALL_IMAGE_HEIGHT": 270,
        "SMALL_IMAGE_STEP": 462,
        "SCORE_OFFSET": -50
    }
}

# 一些位置相关的配置，因为截图的手机不同，所以可能需要适当调整
COVER_1_OFFSET = CONFIG[SNAPSHOT_DEVICE_WIDTH]["COVER_1_OFFSET"]  # 遮盖区1的偏移量，正数右移／负数左移
COVER_1_WIDTH = CONFIG[SNAPSHOT_DEVICE_WIDTH]["COVER_1_WIDTH"]  # 遮盖区1的偏移量，正数右移／负数左移
COVER_2_OFFSET = CONFIG[SNAPSHOT_DEVICE_WIDTH]["COVER_2_OFFSET"]  # 遮盖区2的偏移量，正数右移／负数左移
COVER_2_WIDTH = CONFIG[SNAPSHOT_DEVICE_WIDTH]["COVER_2_WIDTH"]
COVERED_PICTURE = 'picture_with_covered_area.jpg'  # 带遮盖区的图片名称
UPPER_BOUNDRY = CONFIG[SNAPSHOT_DEVICE_WIDTH]["UPPER_BOUNDRY"]
SMALL_IMAGE_HEIGHT = CONFIG[SNAPSHOT_DEVICE_WIDTH]["SMALL_IMAGE_HEIGHT"]
SMALL_IMAGE_STEP = CONFIG[SNAPSHOT_DEVICE_WIDTH]["SMALL_IMAGE_STEP"]
# 比赛关键信息区域截图
RANK_OFFSET = CONFIG[SNAPSHOT_DEVICE_WIDTH]["RANK_OFFSET"]  # 排名左边界的偏移量，正数右移／负数左移
NAME_OFFSET = CONFIG[SNAPSHOT_DEVICE_WIDTH]["NAME_OFFSET"]  # 昵称左边界的偏移量，正数右移／负数左移
SCORE_OFFSET = CONFIG[SNAPSHOT_DEVICE_WIDTH]["SCORE_OFFSET"]  # 分数左边界的偏移量，正数右移／负数左移

if BLACK_ON_RIGHT and SNAPSHOT_DEVICE_WIDTH == "1500":
    RANK_OFFSET = CONFIG[SNAPSHOT_DEVICE_WIDTH]["RANK_OFFSET"] - 52

# 固定配置，别修改
ocr_app_id = "2123257550"
ocr_app_key = "fphTgDZTkmZ200xk"
# 当前家族的成员列表，直接从大表中复制出来即可
MEMBER = "members.txt"
# 机甲或者机甲师名单，一行一个人
MACHINE = "machine.txt"
