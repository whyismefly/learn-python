#!/usr/bin/python
# encoding:utf-8

from sys import argv
scripts,filename=argv

txt=open(filename)

print "here's your file %r:"%filename
print txt.read()

print "type the filename again:"
file_again=raw_input(">")

txt_again=open(file_again)

print txt_again.read()

"""
Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\Administrator>cd E:/GITHUBWORK/learn-python/hardway
C:\Users\Administrator>e:
E:\GITHUBWORK\learn-python\hardway>python hardway15.py ex15_sample.txt
here's your file 'ex15_sample.txt':
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
type the filename again:
>ex15_sample.txt
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
"""