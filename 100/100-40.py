#!/usr/bin/python
# encoding:utf_8

# 题目：将一个数组逆序输出。
# 程序分析：用第一个与最后一个交换。

num=[6, 21, 56, 63, 65, 165, 165, 415, 516, 463,463,464,464,654]

num.reverse()
print num

for i in range(int(len(num)/2)):
    num[i],num[-1-i]=num[-1-i],num[i]
print num