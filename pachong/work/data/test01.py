#!/usr/bin/python
# encoding:utf-8

import requests
from bs4 import BeautifulSoup


#获取百度首页新闻
url="http://www.baidu.com"
req=requests.get(url)
print req.cookies
print type(req.cookies)
# soup=BeautifulSoup(req.content,"lxml").prettify()
# print soup

# LOGIN_URL = 'http://www.baidu.com'  #请求的URL地址
# DATA = {"username":'accountID',"passwd":'passwd'}   #登录系统的账号密码,也是我们请求数据
#
# HEADERS = {
#             'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' #模拟登陆的浏览器
#            }
# RES = requests.post(LOGIN_URL,data=DATA,headers=HEADERS)  #模拟登陆操作
# print (RES.text) #打印返回的文本信息
