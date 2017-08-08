#!/usr/bin/python
# encoding:utf-8

i=0
numbers=[]

while i<6:
    print "at the top i is %d"%i
    numbers.append(i)

    i+=1
print "num now:",numbers

for num in numbers:
        print  num