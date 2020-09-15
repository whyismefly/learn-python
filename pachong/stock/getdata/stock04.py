#!/usr/bin/python
# encoding:utf-8

import retest

line = "Cats are smarter than dogs";

matchObj = retest.match(r'dogs', line, retest.M | retest.I)
if matchObj:
    print "match --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"

matchObj = retest.search(r'dogs', line, retest.M | retest.I)
if matchObj:
    print "search --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"


phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = retest.sub(r'#.*$', "", phone)
print "电话号码是: ", num

# 删除非数字(-)的字符串
num = retest.sub(r'\D', "", phone)
print "电话号码是 : ", num