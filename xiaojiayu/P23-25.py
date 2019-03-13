#!/usr/bin/python3
# encoding:utf-8

import sys
sys.setrecursionlimit(100)

def back():
    return back()

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

# number=int(input("input:"))
# result=fact(number)
# print("%d 的阶成是：%d"%(number,result))
# back()


#斐波拉锲数列
#迭代在函数内某条件下循环执行，递归在函数内某条件下循环调用自己
#迭代
def fab1(n):
    n1=1
    n2=1
    n3=1
    if n<1:
        print("wrong")
        return -1
    while(n-2)>0:
        n3=n2+n1
        n1=n2
        n2=n3
        n-=1
    return n2
# result1=fab1(35)
# if result1!=-1:
#     print("一共%d"%result1)

#递归：
def fab(n):
    if n<1:
        print("cuo!")
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)

# result=fab(35)
# if result!=-1:
#     print("一共%d"%(result))


#汉诺塔问题
def hanoi(n,x,y,z):
    if n==1:
        print(x,"-->",z)
    else:
        hanoi(n-1,x,z,y)
        #将前n-1个盘子从x移动到y上
        print(x,"-->",z)#将最底下的最后一个盘子从x移动到z上
        hanoi(n-1,y,x,z)
n=int(input("层数:"))
hanoi(n,"X","Y","Z")