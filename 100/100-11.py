#!/usr/bin/python
#encoding:utf-8
#  Python练习题要求如下：
#简述：话说有一对可爱的兔子，出生后的第三个月开始，每一月都会生一对小兔子。当小兔子长到第三
# 个月后，也会每个月再生一对小小兔子.
# 问题：假设条件，兔子都不死的情况下，问每个月的兔子总数为多少？

#正常计算
time=int(input("time:"))
x=1
y=1
if (time==1)or(time==2):
    print(y)
for i in range(time-2):
        # z=x+y
        # x=y
        # y=z
        #下面是简写
        x,y=y,x+y
print(y)

#递归recursion
def rabbit(time):
    m1=1
    m2=2
    if time==1 or time==2:
        return 1
    else:
        return rabbit(time - 1) + rabbit(time - 2)
print(rabbit(time))