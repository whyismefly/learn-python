#!/usr/bin/python
#encoding:utf-8

# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 程序分析：请抓住分子与分母的变化规律。

#递归
def shuzi(x):
    if x==1:
        return 1
    if x==2:
        return 2
    else:
        return int(shuzi(x-1)+shuzi(x-2))
y=0
for i in range(1,21):
    y += float(shuzi(i +1)) / float(shuzi(i))
    print i,":",y

#普通
a=1.0
b=1.0
s=0
for i in range(1,21):
    a,b=b,a+b
    s+=b/a
    print i,":",a," ",b," ",s