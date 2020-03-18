#!/usr/bin/python3
# encoding:utf-8

import pymysql
import jieba.analyse
import re
from collections import Counter

# conn=pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="jxw", charset='utf8')
# conn.query()
# conn.commit()
# conn.close()
jxwfile = "G:/jxw1.txt"
file_userdict = "G:/userdict.txt"
# https://blog.csdn.net/Ge0022/article/details/84111058
# https://cloud.tencent.com/developer/article/1487039
def cut_word(datapath):
    jieba.load_userdict(file_userdict)
    with open(datapath,'r',encoding='utf-8')as fp:
        string = fp.read()
        data = re.sub(r"[\s+\.\!\/_,$%^*(【】：\]\[\-:;+\"\']+|[+——！，。？、~@#￥%……&*（）]+|[0-9]+", "", string)
        word_list = jieba.cut(data)

        return word_list


def static_top_word(word_list,top=200):
    counts = {}
    for word in word_list:
        if len(word) == 1:  # 忽略标点符号和其它长度为1的词
            continue
        else:
            counts[word] = counts.get(word, 0) + 1

        # if len(word) == 1:
        #     counts[word] = counts.get(word, 0) + 1
        # else:
        #     continue
    result = dict(Counter(counts))
    sortlist = sorted(result.items(),key=lambda x:x[1],reverse=True)
    resultlist = []
    for i in range(0,top):
        resultlist.append(sortlist[i])
    return resultlist

def record_result(result):
    with open("G:/result.txt",'w',encoding='utf-8')as fp:
        for list in result:
            fp.write(str(list)+'\n')
    print("result ok")



word_list = cut_word(jxwfile)
Result = static_top_word(word_list)
record_result(Result)
