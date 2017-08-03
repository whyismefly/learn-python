#!/usr/bin/python
# encoding:utf-8

from sys import argv

script,user_name=argv
prompt='>'

print "hi %s,i'm the %s script"%(user_name,script)
print "ask you"
print "do you like me %s"%user_name
likes=raw_input(prompt)

print "do you LIVE  %s"%user_name
lives=raw_input(prompt)

print "YOUR COMPUTER %s"%user_name
computer=raw_input(prompt)

print """alringht,so %r ABOUT me,live in %r,your %r computer"""%(likes,lives,computer)

# Microsoft Windows [版本 6.1.7601]
# 版权所有 (c) 2009 Microsoft Corporation。保留所有权利。
#
# C:\Users\Administrator>d E:/GITHUBWORK/learn-python/hardway
# 'd' 不是内部或外部命令，也不是可运行的程序
# 或批处理文件。
#
# C:\Users\Administrator>cd E:/GITHUBWORK/learn-python/hardway
#
# C:\Users\Administrator>s
# 's' 不是内部或外部命令，也不是可运行的程序
# 或批处理文件。
#
# C:\Users\Administrator>e;
# 'e' 不是内部或外部命令，也不是可运行的程序
# 或批处理文件。
#
# C:\Users\Administrator>e:
#
# E:\GITHUBWORK\learn-python\hardway>python hardway14.py
# Traceback (most recent call last):
#   File "hardway14.py", line 6, in <module>
#     script,user_name=argv
# ValueError: need more than 1 value to unpack
#
# E:\GITHUBWORK\learn-python\hardway>python hardway14.py  yes ahat hello
# Traceback (most recent call last):
#   File "hardway14.py", line 6, in <module>
#     script,user_name=argv
# ValueError: too many values to unpack
#
# E:\GITHUBWORK\learn-python\hardway>python hardway14.py  yes ahat
# Traceback (most recent call last):
#   File "hardway14.py", line 6, in <module>
#     script,user_name=argv
# ValueError: too many values to unpack
#
# E:\GITHUBWORK\learn-python\hardway>python hardway14.py  yes
# hi yes,i'm the hardway14.py script
# ask you
# do you like me yes
# >
# do you LIVE  yes
# >3243
# YOUR COMPUTER yes
# >5435
# alringht,so '' ABOUT me,live in '3243',your '5435' computer
#
# E:\GITHUBWORK\learn-python\hardway>^A