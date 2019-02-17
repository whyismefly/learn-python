#!/usr/bin/python
# encoding:utf-8

str1="{0}  is  {1} from {2}"
str2=str1.format("fdwaf","ferwfgre","hrthtr")
#必须是0,1,2...顺序排列，否则报错
print str1
print str2

str3="{a} is {b} of {c}"
str4=str3.format(a="fdwaf",b="ferwfgre",c="hrthtr")
print str3
print str4

print "{{0}}".format("fjodwafj")
#这里0给解释器解释掉了

print "{0:.1f}{1}".format(27.658,"GB")

print '%c' % 97

print " \a "