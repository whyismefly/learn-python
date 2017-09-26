#!/usr/bin/python
# encoding:utf_8

# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。
# 程序分析：无
goon=True
while goon:
    x=int(raw_input("num:"))
    y=x**2
    if y<50:
        goon=False