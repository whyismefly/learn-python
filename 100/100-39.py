#!/usr/bin/python
# encoding:utf-8

# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

num=[165,165,63,654,21,6,516,415,65,56]
num.sort()
x=18
list=[]
for i in range(len(num)):
    if x>num[i]:
        list[i]=num[i]
        break
    else:
        list.append(x)
