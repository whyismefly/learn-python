#!/usr/bin/python
# encoding:utf-8

from sys import argv

script,first,second,third=argv

print "script 1",script
print "first ",first
print "second ",second
print "third ",third



#这个需要从别处调用hardway13.py这个文件并附带参数，都则会报错

# D:\PYTHON\Python27\python.exe E:/GITHUBWORK/learn-python/hardway/hardway13.py
# Traceback (most recent call last):
#   File "E:/GITHUBWORK/learn-python/hardway/hardway13.py", line 6, in <module>
#     script,first,second,third=argv
# ValueError: need more than 1 value to unpack


# Microsoft Windows [版本 6.1.7601]
# 版权所有 (c) 2009 Microsoft Corporation。保留所有权利。
#
# C:\Users\Administrator>cd E:/GITHUBWORK/learn-python/hardway
# C:\Users\Administrator>python hardway13.py
# python: can't open file 'hardway13.py': [Errno 2] No such file or directory
# C:\Users\Administrator>
# C:\Users\Administrator>e
# 'e' 不是内部或外部命令，也不是可运行的程序
# 或批处理文件。
# C:\Users\Administrator>e:
# E:\GITHUBWORK\learn-python\hardway>python hardway13.py
# Traceback (most recent call last):
#   File "hardway13.py", line 6, in <module>
#     script,first,second,third=argv
# ValueError: need more than 1 value to unpack
# E:\GITHUBWORK\learn-python\hardway>python hardway13.py first 2nd 3rd
# script 1 hardway13.py
# first  first
# second  2nd
# third  3rd
#
# E:\GITHUBWORK\learn-python\hardway>python hardway13.py first 2nd
# Traceback (most recent call last):
#   File "hardway13.py", line 6, in <module>
#     script,first,second,third=argv
# ValueError: need more than 3 values to unpack
#
