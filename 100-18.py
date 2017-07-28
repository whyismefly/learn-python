#!/usr/bin/python
#encoding:utf-8

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
#
# 程序分析：关键是计算出每一项的值。

num=input("num")
nextnum=num
y=nextnum
time=input("time")
if time==1:
    print num
else:
    for i in range(time-1):
        nextnum=nextnum*10+num
        y=y+nextnum
        print nextnum
    print y
