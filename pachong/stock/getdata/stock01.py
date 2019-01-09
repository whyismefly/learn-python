#!/usr/bin/python
# encoding:utf-8


import urllib
import requests
from bs4 import BeautifulSoup
import sqlite3

#获取网页urllib
def gethtmlbyurllib(url):
    page =urllib.urlopen(url)
    html=page.read()
    return html

#获取网页bs4
def gethtmlbybs4(url):
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"lxml")
    items=soup.find('a')
    # print soup
    # print type(soup.head)
    # print soup.title
    # print type(soup.title)
    # print soup.a.name
    # print soup.a.attrs

# 保存网页
def savehtmlastxt(html,savename):
    # html = open(str(savename)+".html", "wb")
    #中文会出现乱码
    html = open(unicode(str(savename) + ".html","utf-8"), "wb")
    try:
        html.write(h)
    finally:
        html.close()

#提取网页信息/正则
def selectinfomation(html):
    print "hello"

#测试

# #东方财富网
h = gethtmlbyurllib("http://quote.eastmoney.com/stocklist.html")
savehtmlastxt(h,"股票名称编号")

#遍历文件夹并获取特定类型文件
# import os
#
#
# def file_name(file_dir):
#     L = []
#     for root, dirs, files in os.walk(file_dir):
#         for file in files:
#             if os.path.splitext(file)[1] == '.jpeg':
#                 L.append(os.path.join(root, file))
#     return L

#获取指定文件内容
# try:
#     f = open('/path/to/file', 'r')
#     print f.read()
# finally:
#     if f:
#         f.close()
#
# with open('/path/to/file', 'r') as f:
#     print f.read()