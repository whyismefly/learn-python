#!/usr/bin/python
#encoding:utf-8

# 题目：利用递归方法求5!。


def fn(n):
    if n==1:
        return 1
    else:
        return fn(n-1)*n
print(fn(5))


