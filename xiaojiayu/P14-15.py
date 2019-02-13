#!/usr/bin/python
# encoding:utf-8

#元组  不可直接修改  字符串类似于元组
tuple1=(1,2,3,4,5,6,7,8,9,)
print tuple1[5:]
print tuple1[:5]
temp=1
print type(temp)
temp2=25,3,4
print type(temp2)
temp=1,
print type(temp)
temp=(1,)
print type(temp)
temp=("fwhruifhei",2123123,"fhoierqwhfrei,","fhuirhfgrfgggbmkkh")
temp=temp[:2]+("jfowhjf",)+temp[2:]
print temp

str1='fjeriop gjgp mrhp[krthrgt'
print (str1.capitalize())
#尝试一下str的各种方法吧