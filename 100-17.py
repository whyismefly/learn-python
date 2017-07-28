#!/usr/bin/python
#encoding:utf-8

# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#
# 程序分析：利用while语句,条件为输入的字符不为'\n'。

"""
whitespace -- a string containing all characters considered whitespace
lowercase -- a string containing all characters considered lowercase letters
uppercase -- a string containing all characters considered uppercase letters
letters -- a string containing all characters considered letters
digits -- a string containing all characters considered decimal digits
hexdigits -- a string containing all characters considered hexadecimal digits
octdigits -- a string containing all characters considered octal digits
punctuation -- a string containing all characters considered punctuation
printable -- a string containing all characters considered printable
"""

import string
str1=raw_input('string:')
#在PYTHON3中可以直接使用input()
english=0
space=0
num=0
other=0
for i in str1:
    if i.isalpha():
        english+=1
    elif i.isspace():
        space+=1
    elif i.isdigit():
        num+=1
    else:
        other+=1
print('char=char = %d,space = %d,digit = %d,others = %d' % (english,space,num,other))