#!/usr/bin/python
# encoding:utf-8

import sys
sys.path.append("E:/GITHUBWORK/learn-python/pachong/stock")
# sys.path.append("../getdata") 这样解决不了问题
from getdata import stock01

url="http://quote.eastmoney.com/stocklist.html"
# htmllib = stock01.gethtmlbyurllib(url)
htmlbs4=stock01.gethtmlbybs4(url)
print htmlbs4
