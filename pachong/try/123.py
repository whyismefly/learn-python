#!/usr/bin/python
# encoding:utf-8
import retest
a = "123abc456"
print retest.search("([0-9]*)([a-z]*)([0-9]*)", a).group(0)   #123abc456,返回整体
print retest.search("([0-9]*)([a-z]*)([0-9]*)", a).group(1)   #123
print retest.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2)   #abc
print retest.search("([0-9]*)([a-z]*)([0-9]*)", a).group(3)   #456
print retest.search("([0-9]*)([a-z]*)([0-9]*)", a).group()

