#!/usr/bin/python
# encoding:utf-8

#题目：查找字符串。

str1 = '我的违反公务二级服务机构评为二级佛为'
str2 = '二级'
print str1.find(str2)
print "-"*30
str3 = 'abbbbbbbbbbbbbabbbbbbbbbbbccccccccccccccccccccccccddddddddd'
str4 = 'ab'
print str3.find(str4)
print str3.index(str4)
print str3.count('ab')
print "-"*30
s = 'eyou me heEEEEEEEEEEEEEEEeeeeeeeeeeeee'
index=-1
while True:
    index = s.find('e',index+1)
    """下次查询从下一位开始"""
    if index==-1:
        break
    print index

s = 'you me he'
s = list(s)
while(1):
     if 'e' in s:
            index = s.index('e')
            print index
            s[index] = '*'
            """若注释了则无线循环输出"""
     else:
             break
