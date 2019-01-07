#!/usr/bin/python
# encoding:utf-8

import urllib
import re
import requests
import bs4
from bs4 import BeautifulSoup

#打开目标网页
url="http://quote.eastmoney.com/stocklist.html"
req=requests.get(url)
soup=BeautifulSoup(req.content,"lxml")

#输出标准网页
# items=soup.find('a')
x=soup.prettify()
# print soup
print "输出标准网页",'-'*150

#获取标题
# print soup.title
# print type(soup.title)
# print soup.title.name
# print soup.title.attrs
# print soup.title.get_text()
print "获取标题",'-'*150

#尝试获取特定内容
#select选择特定组件在特定名称组件前面加.也就是.name去找组件，再往下细分的话就是类似于 a b c这种层次
# print soup.ul.li
# print soup.ul.li.get_text()
# print soup.find_all(re.compile('^li'))
# print soup.find_all('/li')
# print soup.select('.quotebody ul li')



print "尝试获取特定内容",'-'*180

#获取股票代码和名称
# print x.find_all('a')
# for tag in soup.find_all('div', class_='info'):
# m_name = tag.find('span', class_='title').get_text()
# m_rating_score = float(tag.find('span',class_='rating_num').get_text())
# m_people = tag.find('div',class_="star")
# m_span = m_people.findAll('span')
# m_peoplecount = m_span[3].contents[0]
# m_url=tag.find('a').get('href')
# print( m_name+"        "  +  str(m_rating_score)   + "           " + m_peoplecount + "    " + m_url )
print "获取股票代码和名称",'-'*180

def savehtmlastxt(html,savename):
    # html = open(str(savename)+".html", "wb")
    #中文会出现乱码
    html = open(unicode(str(savename) + ".html","utf-8"), "wb")
    try:
        html.write()
    finally:
        html.close()