#!/usr/bin/python
#encoding:utf-8

# 题目：求1+2!+3!+...+20!的和。
# 程序分析：此程序只是把累加变成了累乘。
x=1
y=0
z=20
for i in  range(1,z+1):
    x=x*i
    y+=x
    print (x,y)