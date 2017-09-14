#!/usr/bin/python
# encoding:utf-8

# 题目：求100之内的素数。
# 程序分析：无。

import math

for i in range(3,101):
    j=2
    x=i%j
    if x!=0:
        print i
    else:
        j+=1