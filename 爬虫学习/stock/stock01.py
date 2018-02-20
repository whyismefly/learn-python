#!/usr/bin/python
# encoding:utf-8

import urllib
import sqlite3

#获取网页
def gethtml(url):
    page =urllib.urlopen(url)
    html=page.read()
    return html


# 保存网页
def savehtmlastxt(html):
    html = open("1.html", "wb")
    try:
        html.write(h)
    finally:
        html.close()

h = gethtml("https://www.cnblogs.com/snowbook/p/5764549.html")
savehtmlastxt(h)



# try:
#     f = open('/path/to/file', 'r')
#     print f.read()
# finally:
#     if f:
#         f.close()
#
# with open('/path/to/file', 'r') as f:
#     print f.read()