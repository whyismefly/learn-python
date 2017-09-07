#!/usr/bin/python
# encoding:utf-8

# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

intnum=input("number:")
num=str(intnum)

x=len(num)
flag=True
for i in range(x/2):
    if num[i]!=num[-i-1]:
        flag=False
        break
    else:
     flag=True
if flag:
    print "yes"
else:
    print "no"


