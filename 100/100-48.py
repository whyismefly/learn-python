#!/usr/bin/python
# encoding:utf_8

# 题目：数字比较。

def compare(a,b):
    if a>b:
        print a,">",b
    elif a==b:
        print a,"=",b
    elif a<b:
        print a,"<",b

compare(3,6)