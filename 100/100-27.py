#!/usr/bin/python
#encoding:utf-8

#无递归
l=input("a string:")
m=int(len(l))
for i in range(m,0,-1):
    print(l[i-1])


#递归
def out(l,m):
    if m==0:
        return 0
    print(l[m-1])
    out(l,m-1)
out(l,m)