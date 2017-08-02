#!/usr/bin/python
#encoding:utf-8

#  问题简述：假设一支皮球从100米高度自由落下。条件，每次落地后反跳回原高度的一半后，再落下。
#
# 要求：算出这支皮球，在它在第10次落地时，共经过多少米？第10次反弹多高？

time=10
height=100.0
distance=100.0
if time==1:
    print(distance)
else:
    for i in range(1,time):
        height=height/2
        distance=distance+(2*height)
    print(distance)
    print(height)

