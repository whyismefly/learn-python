#!/usr/bin/python
# encoding:utf-8

import urllib
from bs4 import BeautifulSoup

res = urllib.urlopen("http://www.baidu.com")
print res.read()
print "*"*150
url = "http://www.baidu.com"
page = urllib.urlopen(url)
soup = BeautifulSoup(page,"html.parser")
print soup