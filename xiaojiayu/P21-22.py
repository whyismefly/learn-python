#!/usr/bin/python3
# encoding:utf-8

count=5
def Func():
    count=10
    print(count)

Func()
print(count)

def fun1():
    print(11111111111)
    def fun2():
        print(222222222)
    fun2()
fun1()

def fun3(x):
    def fun4(y):
        return x*y
    return fun4
i=fun3(5)
print(type(i))
print(i)
print(type(fun3))
print(type(fun3(6)))
print(i(8))
print(fun3(6)(7))
print(fun3(8))

def fun3():
    x=5
    def fun4():
        nonlocal x
        x *= x
        return x
    return fun4

x=lambda x:2*x+1  #匿名函数，用后即删

print(filter(None,[1,2,3,4,5,0,False,True]))
#filter只返回真值
print(list(filter(None,[1,2,3,4,5,0,False,True])))
print(list(filter(lambda x: x%2,range(100))))
print(list(map(lambda x:  x%2,range(100))))

def f(x):
    return x*x
print(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))



