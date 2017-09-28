#!/usr/bin/python
# encoding:utf-8

import urllib
from bs4 import BeautifulSoup
import re

# res = urllib.urlopen("http://www.baidu.com")
# print res.read()
# print "*"*150
# url = "http://www.sohu.com/"
# page = urllib.urlopen(url)
# soup = BeautifulSoup(page,"html.parser")
# print soup

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')
pattern.sub()
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')

if match:
    # 使用Match获得分组信息
    print match.group()

    ### 输出 ###
    # hello