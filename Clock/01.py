#!/usr/bin/python
# encoding:utf-8

import time
import timeit
# control=1
# while control:
#         t = time.time()
#         print "%s\r" % t,

def func1():
    s = 0
    for i in range(1000):
        s += i
    print(s)

# timeit(函数名_字符串，运行环境_字符串，number=运行次数)
t = timeit('func1()', 'from __main__ import func1', number=1000)
print(t)