#!/usr/bin/python
# encoding:utf-8

# 题目：求100之内的素数。
# 程序分析：无。

for i in range(2,101):
        for j in range(2,i):
            x=i%j
            if x==0:
                break
        else:
                print i

