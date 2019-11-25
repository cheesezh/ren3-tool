# !/usr/bin/env python
# encoding: utf-8

"""
@Author  : hezhang
@Email   : hezhang@mobvoi.com
@Time    : 2019/10/26 下午11:41
@File    : all_members.py
@IDE     : PyCharm
"""
import math
import config
import codecs

INACTIVE_INFO = "-\t-\t-\t0"  # 未请假未参战

def search(name, info):
    max_score = -1
    result = INACTIVE_INFO
    rslt_key = ""
    epsilon = 1e-5
    confidence = 0.0
    for key in info.keys():
        match_score = 0
        match_score2 = 0
        tmp_key = key.replace("Night☆", "")
        for i in name:
            if i in tmp_key:
                match_score += 1
        for j in tmp_key:
            if j in name:
                match_score2 += 1

        if match_score + match_score2 > max_score:
            max_score = match_score + match_score2
            result = info[key]
            rslt_key = key
            confidence = math.log(epsilon + 1.0 * match_score / (1 + len(name))) \
                         + math.log(epsilon + match_score2 / (1 + len(tmp_key))) * -10
    ret = "{}".format(result) if confidence < 10 else INACTIVE_INFO
    if ret == INACTIVE_INFO:
        rslt_key = ""
    return ret, rslt_key

if __name__ == "__main__":
    # 根据截图生成的参战信息
    info = {}
    # 参战并且被匹配到
    info_found = set()

    suffix_idx = config.FILE_NAME.rfind(".")
    file_name = config.FILE_NAME[0:suffix_idx]
    with codecs.open("{}-reformat.txt".format(file_name), 'r', 'utf8') as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            cks = line.split("\t")
            name = cks[1]
            if name not in info:
                info[name] = line

    final_rslt = ["简称\t团战排名\t游戏昵称\t团战得分\t团战等级"]
    with codecs.open(config.MEMBER, "r", "utf8") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                final_rslt.append("")
                print("")
                continue
            rslt, name = search(line, info)
            info_found.add(name)
            rslt = "{}\t{}".format(line, rslt)
            final_rslt.append(rslt)
            print(rslt)
    with codecs.open("{}-final.txt".format(file_name), 'w', 'utf8') as f:
        f.write("\n".join(final_rslt))

    with codecs.open("{}-no-found.txt".format(file_name), 'w', 'utf8') as f:
        for k in info:
            if k not in info_found:
                f.write(info[k] + "\n")

    print("\n已生成最终文件 [{}-final.txt] 以及未找到名单 [{}-no-found.txt] ".format(file_name, file_name))
    print("下一步需人工校验结果。")
