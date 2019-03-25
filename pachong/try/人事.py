#!/usr/bin/python
# encoding:utf-8

"""
# import re
# import urllib
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
# import csv
# import html5lib#使用read_html()时出现ImportError: html5lib not found, please install it
from sqlalchemy import create_engine


"""
# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html

# def getImg(html):
#     reg = r'src="(.+?\.jpg)" pic_ext'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre,html)
#     x = 0
#     for imgurl in imglist:
#         urllib.urlretrieve(imgurl,'%s.jpg' % x)
#         x+=1

# print getImg(html)

# m110="http://www.apta.gov.cn/Officer/Summary?examid=64&&pcode=&pi=4"
# m150="http://www.apta.gov.cn/Officer/Summary?examid=64&&pcode=&pi=5"
# m520="http://www.apta.gov.cn/Officer/Summary?examid=64&&pcode=&pi=12"
# 
# h110=getHtml(m110)
# h150=getHtml(m150)
# h520=getHtml(m520)
# print h110,h150,h520

# m520="http://134.64.116.90:8030/sdp/p1446609752151_AutoCreateZul_9.zul;Managed_Server_Name=134.64.70.56:8020"
# h520=getHtml(m520)
# print h520
"""


url_first="http://www.apta.gov.cn/Officer/Summary?examid=90&pi="

for page in range(1,56):#一共55页
    url_all=url_first+str(page)
    req = requests.get(url_all)
    soup = BeautifulSoup(req.text, "lxml")
    tb = pd.read_html(soup.prettify(),header = 0)[4]  # 经观察人事考试网中所需表格是网页中第5个表格，故为[4]
    engine = create_engine('mysql://root:root@localhost:3306/stock_test?charset=utf8')
    tb.to_sql('renshiwang2', engine, if_exists='append')
    df1 = pd.read_sql('renshiwang2', engine)

