#!usr/bin/python
# encoding:utf-8
# Python练习题问题如下：
# 简述：这里有四个数字，分别是：1、2、3、4
# 提问：能组成多少个互不相同且无重复数字的三位数？各是多少？
x=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j)and(i!=k)and(k!=j):
                print(i,j,k)
                x+=1
print(x)