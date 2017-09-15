#!/usr/bin/python
# encoding:utf-8

# 题目：对10个数进行排序。
# 程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二
# 个元素与后8个进行比较，并进行交换。

num=[165,165,63,654,21,6,516,415,65,56]
num.sort()
print num
num.reverse()
print num

print len(num)
print num[2]