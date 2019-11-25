# !/usr/bin/env python
# encoding: utf-8

"""
@Author  : hezhang
@Email   : hezhang@mobvoi.com
@Time    : 2019/10/26 下午10:39
@File    : reformat.py
@IDE     : PyCharm
"""

import config
import re
import sys
import codecs

if __name__ == "__main__":
    suffix_idx = config.FILE_NAME.rfind(".")
    file_name = config.FILE_NAME[0:suffix_idx]

    with codecs.open('{}-ocr.txt'.format(file_name), 'r', 'utf8') as f:
        lines = f.readlines()
        rslt = []
        previous = 0
        last_idx = int(lines[-3])

        for i in range(0, len(lines), 3):
            try:
                nick_name = lines[i+1].strip()
                nick_name = re.sub('([NM]ight.)', 'Night☆', nick_name)
                nick_name = nick_name.replace('Night☆', '')
                # 成绩排名
                rank_value = int(lines[i].strip())

                # 20191116新规则：族战团本前5记录5，前30记录3，参战记录1
                if rank_value <= 5:
                    rank = "5"
                elif rank_value <= 30:
                    rank = "3"
                else:
                    rank = "1"

                line = "{}\t{}\t{}\t{}".format(rank_value, nick_name, lines[i+2].strip(), rank)
                if rank_value != previous + 1:
                    raise Exception("ERROR")
                else:
                    previous = rank_value
                print(line)
                rslt.append(line)
            except:
                print("=" * 10)
                print("请检查[{}-ocr.txt]文件，第[ {} ]名后的信息有误。".format(file_name, previous))
                print("可能有以下错误:\n"
                      "1.缺少排名信息\n"
                      "2.缺少成绩信息(例如'神经元4067'连在一起了)\n"
                      "3.重复信息，一个玩家被截图两次截到")
                sys.exit(-1)

    with codecs.open("{}-reformat.txt".format(file_name), 'w', 'utf8') as f:
        f.write("\n".join(rslt))

    print("\n已调整自动识别结果文件格式：{}-reformat.txt".format(file_name))
    print("下一步请执行命令：python 3-gen-final-info.py")