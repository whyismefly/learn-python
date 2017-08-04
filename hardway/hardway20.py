#!/usr/bin/python
#encoding:utf-8

from sys import argv
script,input_file=argv

def print_all(f):
    print f.read()

def reweind(f):
    print f.seek(0)

def print_a_line(line_count,f):
    print line_count,f.readline()
    #注意不是read而是readline

current_file=open(input_file)
print "first print file:\n"
print_all(current_file)

print "now rewind."

reweind(current_file)

print "print three lines:"

current_line=1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

"""
Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\Administrator>cd E:/GITHUBWORK/learn-python/hardway

C:\Users\Administrator>e:

E:\GITHUBWORK\learn-python\hardway>python hardway20.py test.txt
first print file:

fbwuioefherio
reiughopergr
tioiopjghotjhtjph[ktp

now rewind.
None
print three lines:
1 fbwuioefherio

2 reiughopergr

3 tioiopjghotjhtjph[ktp


E:\GITHUBWORK\learn-python\hardway>python hardway17.py
"""