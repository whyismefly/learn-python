#!/usr/bin/python
# encoding:utf-8
import re
# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母


def judge(letter,week):
    list=[]
    letter=letter.upper()
    #转换成大写
    for a in week:
        if re.match(letter,a):
            #匹配功能
            list.append(a)
    if len(list)==1:
            print list[0]
    else:
            secondletter=raw_input("second letter:")
            for b in list:
                if re.match(letter+secondletter,b):
                    print b
list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
first=raw_input('请输入第一个字母：')
judge(first,list)


