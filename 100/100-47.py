#!/usr/bin/python
# encoding:utf_8
# 题目：两个变量值互换。
# 程序分析：无

a=10
b=8
def exchange(a,b):
    a, b = b, a
    print a,b

print a,b
exchange(a,b)