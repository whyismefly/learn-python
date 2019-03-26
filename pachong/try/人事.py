#!/usr/bin/python
# encoding:utf-8

"""
# import re
# import urllib
"""

#先安装html5lib
from bs4 import BeautifulSoup
import requests
import pandas as pd
# import csv
# import html5lib#使用read_html()时出现ImportError: html5lib not found, please install it
from sqlalchemy import create_engine
import datetime


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

def getlist():
    try:
        url_first = "http://www.apta.gov.cn/Officer/Summary?examid=90&pi="
        start_time = datetime.datetime.now()
        print str(start_time)+" start"
        for page in range(1, 56):  # 一共55页
            url_all = url_first + str(page)
            # req = requests.get(url_all)
            # https: // blog.csdn.net / weixin_36646275 / article / details / 83965610
            """HTTPConnectionPool（host:XX）Max retries exceeded with url 解决方法
在做双十一压测时,高并发调用requests时报错.问题解决方法
问题原因
是因为在每次数据传输前客户端要和服务器建立TCP连接，为节省传输消耗，默认为keep-alive，即连接一次，传输多次，然而在多次访问后不能结束并回到连接池中，导致不能产生新的连接,headers中的Connection默认为keep-alive，将header中的Connection一项置为close.
"""
            req = requests.get(url_all,headers={"Connection": "close"})
            soup = BeautifulSoup(req.text, "lxml")
            tb = pd.read_html(soup.prettify(), header=0)[4]  # 经观察人事考试网中所需表格是网页中第5个表格，故为[4]
            engine = create_engine('mysql://root:root@localhost:3306/stock_test?charset=utf8')
            tb.to_sql('renshiwang2', engine, if_exists='append')
            df1 = pd.read_sql('renshiwang2', engine)
        end_time=datetime.datetime.now()
        print str(end_time)+" LIST DONE"
    except Exception,e:
        end_time = datetime.datetime.now()
        print str(end_time)+" Exception:"
        print e

if __name__ == '__main__':
    getlist()
