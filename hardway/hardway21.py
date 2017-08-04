#!/usr/bin/python
#encoding:utf-8

def add(a,b):
    print "adding %d + %d"%(a,b)
    return a+b

def subtract(a,b):
    print "subtracting %d - %d"%(a,b)
    return a-b

def multiply(a, b):
    print "multiplying %d * %d" % (a, b)
    return a*b

def divide(a, b):
    print "dividing %d / %d" % (a, b)
    return a/b

print "do math"

age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print "age:%d,height:%d,weight:%d,iq:%d"%(age,height,weight,iq)

print "a puzzle."

what=add(age,subtract(height,multiply(weight,divide(iq,2))))
print "become:",what,"can you do it by hand?"
a=24+34/100-1023
print a

# Remember int(raw_input())? The problem with that is then you can’t enter fl oating point, so
# also try using float(raw_input()) instead.