# !/usr/bin/env python
# encoding: utf-8

"""
@Author  : hezhang
@Email   : hezhang@mobvoi.com
@Time    : 2019/10/26 上午8:48
@File    : cut.py
@IDE     : PyCharm
"""

from config import ocr_app_id, ocr_app_key
import config
import os
import time
import base64
import hashlib
import random
import string
from urllib.parse import quote
import requests
import codecs


def curlmd5(src):
    m = hashlib.md5(src.encode('UTF-8'))
    return m.hexdigest().upper()

# 请求时间戳（秒级），用于防止请求重放（保证签名5分钟有效）
def get_params(base64_data):
    t = time.time()
    time_stamp = str(int(t))
    # 请求随机字符串，用于保证签名不可预测
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    # 应用标志，这里修改成自己的id和key
    app_id = ocr_app_id
    app_key = ocr_app_key
    params = {'app_id': app_id,
              'image': base64_data,
              'time_stamp': time_stamp,
              'nonce_str': nonce_str,
              }
    sign_before = ''
    # 要对key排序再拼接
    for key in sorted(params):
        # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写。
        sign_before += '{}={}&'.format(key, quote(params[key], safe=''))
    # 将应用密钥以app_key为键名，拼接到字符串sign_before末尾
    sign_before += 'app_key={}'.format(app_key)
    # 对字符串sign_before进行MD5运算，得到接口请求签名
    sign = curlmd5(sign_before)
    params['sign'] = sign
    return params

def ocr_img(name):
    url = "https://api.ai.qq.com/fcgi-bin/ocr/ocr_handwritingocr"
    with open('tmp{}{}.jpg'.format(os.path.sep, name), 'rb') as fin:
        image_data = fin.read()
    base64_data = base64.b64encode(image_data)
    params = get_params(base64_data)
    r = requests.post(url, data=params)
    item_list = r.json()['data']['item_list']
    res = [i['itemstring'] for i in item_list]
    time.sleep(1)
    return res

print("准备自动识别...")
info_list = []
pic_list = []
for i in os.listdir("tmp"):
    pic_list.append(i.replace(".jpg", ""))

for pic in pic_list:
    new_info = []
    while len(new_info) < 1:
        print("正在解析{}.jpg".format(pic))
        new_info = ocr_img(pic)
    info_list.extend(new_info)

suffix_idx = config.FILE_NAME.rfind(".")
image_name = config.FILE_NAME[0:suffix_idx]

with codecs.open("{}-ocr.txt".format(image_name), 'w', 'utf8') as f:
    f.write("\n".join(info_list))

print("\n已生成自动识别结果文件：{}-ocr.txt".format(image_name))
print("下一步请执行命令：python 2-reformat.py")