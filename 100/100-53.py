#!/usr/bin/python
# encoding:utf_8

# 题目：学习使用按位异或 ^ 。
# 程序分析：0^0=0; 0^1=1; 1^0=1; 1^1=0

a = 77
b = a ^ 3
print 'a ^ b is %d' % b
b ^= 7
print 'a ^ b is %d' % b