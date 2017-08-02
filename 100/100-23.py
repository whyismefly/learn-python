#!/usr/bin/python
#encoding:utf-8

# 题目：打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# 程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。

lie=int(input("lieshu"))
for i in range(1,lie):
        for j in range(lie-i):
            print("-")
        print("\n")
        for j in range(2*i-1):
            print("*")
        print("\n")
for i in range(lie,0,-1):
        for k in range(0,lie-i):
            print("-")
        print("\n")
        for k in range(0,2*i-1):
            print("*")
        print("\n")
