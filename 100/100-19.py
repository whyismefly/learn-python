#!/usr/bin/python
#encoding:utf-8

# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

for i in range(1,100001):
    sum = 0
    #大于一半必然不能分解因子，素数必然不是完数，无需考虑
    for j in range(1,int(i/2+1)):
            if i%j==0:
                sum=sum+j
    if sum==i:
        print (i)


