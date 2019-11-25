# !/usr/bin/env python
# encoding: utf-8

"""
@Author  : hezhang
@Email   : hezhang@mobvoi.com
@Time    : 2019/10/26 下午10:39
@File    : reformat.py
@IDE     : PyCharm
"""

import shenyuan_config as config
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
        last_idx = int(lines[-2])
        for i in range(0, len(lines), 2):
            try:
                rank_value = int(lines[i].strip())
                if rank_value <= 10:
                    rank = "5"
                elif rank_value <= 30:
                    rank = "3"
                else:
                    rank = "1"
                nick_name = lines[i+1].strip()
                nick_name = re.sub('([NM]ight.)', 'Night☆', nick_name)
                line = "{}\t{}\t{}".format(rank_value, nick_name, rank)
                if rank_value != previous + 1:
                    raise Exception("ERROR")
                else:
                    previous = rank_value
                print(line)
                rslt.append(line)
            except:
                print("请检查[{}-ocr.txt]文件.".format(file_name))
                sys.exit(-1)
    with codecs.open("{}-reformat.txt".format(file_name), 'w', 'utf8') as f:
        f.write("\n".join(rslt))