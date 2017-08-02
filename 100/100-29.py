#!/usr/bin/python
#encoding:utf-8

# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# 程序分析：学会分解出每一位数。

import math
#按照字符串方法解析
l=input("num:")
m=len(l)
for i in range(m,0,-1):
    print(l[i-1])

#按照数学方法解析
print( '请输入大于10的数字:' )
n=int(input())
x=[]
i=0;
while(n!=0):
    x.append(n%10)
    i+=1
    n=int(n/10)
print( '该数有 %d 位\n' %i )
print( '逆序为：\n')
print( x[::] )