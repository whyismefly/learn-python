#!/usr/bin/python
# encoding:utf-8

import requests
from bs4 import BeautifulSoup
from lxml import etree


#获取百度首页新闻
url="http://www.baidu.com"
LOGIN_URL="https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F&sms=5"
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


# 这个是网站在登录的时候验证密码的界面，一般不是登录的界面，需要抓包获取到
post_url = "https://pos.XXXX.com/j_security_check"
username = input("请输入登录账号：")
password = input("请输入登录密码：")
session = requests.session()


# 表单数据
data = {
    "j_username": username,
    "j_password": password
}
try:
    login_page = session.post(post_url, data=data, headers=headers)
    if "loginerror" in login_page.text:
        print("登录失败，错误的手机号码或密码！")
    if "</span>首页" in login_page.text:
        print("欢迎您'%s'，成功登陆POS管理系统！" % username)
except Exception as e:
    print(e)

# 需要登录后才能访问的页面网址
url = "https://pos.XXXXX.com/item/itemlist.html"
item_list = session.post(url, headers=headers)
html = etree.HTML(item_list.text)
Total_list = html.xpath('//span[@class="pagebanner"]/text()')
# # 可以将网页保存到本地，便于分析
# with open("test.html", "w", encoding="utf-8")as f:

"""
BDUSS
名称
BDUSS
内容
pyaVhZbE0yNDFzRmV1TlhnWTBVWWF2SVczcE0zd2hFVVNyY2NHeDE3T042bUpjQVFBQUFBJCQAAAAAAAAAAAEAAAD8SIsHd2h5aXNtZWZseQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI1dO1yNXTtcOG
域名
.baidu.com
路径
/
为何发送
各种连接
脚本可访问
否（仅 Http）
创建时间
2019年1月13日星期日 下午11:47:25
到期时间
2027年4月1日星期四 下午11:47:25
"""

