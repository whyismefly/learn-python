#!/usr/bin/python
# encoding:utf-8

#题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

from random import randint

data = [randint(1,100) for i in range(20)]
print(data)

n = 20
m = 5

# data[5:20]= data[0:15]
data[5:20], data[0:5] = data[0:15] ,data[15:20]
print data



