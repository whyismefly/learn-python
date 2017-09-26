#!/usr/bin/python
# encoding:utf-8

# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

num=[6, 21, 56, 63, 65, 165, 165, 415, 516, 463,463,463,464,464,464,464,654]
x=463
print num
for i in range(len(num)):
    if x>num[-1-i]:
        num.insert(-i+1,x)
        break
print num


list=[1,2,3]
list.insert(3,x)
print list
