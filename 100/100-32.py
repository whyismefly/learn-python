#!/usr/bin/python
# encoding:utf-8

# 题目：按相反的顺序输出列表的值。
# 程序分析：无。

def list(time):
    lists=[]
    for i in range(time):
        word=raw_input("input list:")
        lists.append(word)
    return lists

def last2first(list):
    for i in range(len(list)):
        print list[-1-i]

time=int(raw_input("how many words:"))
lis=list(time)
print "-"*20
last2first(lis)
print "-"*20
lis.reverse()
#自带的倒序排序方法
print lis



