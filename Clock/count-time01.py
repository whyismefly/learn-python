#!/usr/bin/python
# encoding:utf-8
#参考
# http://blog.csdn.net/chichoxian/article/details/53108365
#http://blog.csdn.net/gatieme/article/details/45674367

import time
import datetime
import timeit
import platform

def testfunc():
    sum=0
    for i in range(10000):
        sum=sum+1
    print "-"*50
    print sum
    print "-" * 50

def TestPlatform( ):
    print ("----------Operation System--------------------------")
    #  获取Python版本
    print platform.python_version()

    #   获取操作系统可执行程序的结构，，(’32bit’, ‘WindowsPE’)
    print platform.architecture()

    #   计算机的网络名称，’acer-PC’
    print platform.node()

    #获取操作系统名称及版本号，’Windows-7-6.1.7601-SP1′
    print platform.platform()

    #计算机处理器信息，’Intel64 Family 6 Model 42 Stepping 7, GenuineIntel’
    print platform.processor()

    # 获取操作系统中Python的构建日期
    print platform.python_build()

    #  获取系统中python解释器的信息
    print platform.python_compiler()

    if platform.python_branch()=="":
        print platform.python_implementation()
        print platform.python_revision()
    print platform.release()
    print platform.system()

    #print platform.system_alias()
    #  获取操作系统的版本
    print platform.version()
    #  包含上面所有的信息汇总
    print platform.uname()

def UsePlatform( ):
    sysstr = platform.system()
    if(sysstr =="Windows"):
        print ("Call Windows tasks")
    elif(sysstr == "Linux"):
        print ("Call Linux tasks")
    else:
        print ("Other System tasks")

#datetime时间精确度较差
start = datetime.datetime.now()
testfunc()
end = datetime.datetime.now()
print "datetime()", (end-start)

#linux常用
start = time.time()
testfunc()
end = time.time()
print "time()", (end-start),str(end-start)

#windows常用
start =time.clock()
testfunc()
print(sum)
end = time.clock()
print "clock()", (end-start),str(end-start)

#跨平台使用
start = timeit.default_timer()
testfunc()
end = timeit.default_timer()
print "timeit()",(end-start),str(end-start)

#系统检测
TestPlatform()
UsePlatform()
