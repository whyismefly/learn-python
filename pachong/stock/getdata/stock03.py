#!/usr/bin/python
# encoding:utf-8

from abc import ABCMeta, abstractmethod
import re
import requests
from bs4 import BeautifulSoup
import sys
sys.path.append("E:/GITHUBWORK/learn-python/pachong/stock")
import urllib

def gettestsoup():
    try:
        url = "http://quote.eastmoney.com/stocklist.html"
        req = requests.get(url)
        soup = BeautifulSoup(req.content, "lxml")
        # print soup
        return soup
    except (Exception), e:
        print e

def getsoup(url):
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.content, "lxml")
        # print soup
        return soup
    except (Exception), e:
        print e

def getinfo(soup):
    for link in soup.find_all('a'):
        print link.get_text(),
        print(link.get('href'))


line = """</script>
    <div class="qox">
        <div class="space3">
        </div>
        <div class="quotebody">
            <div id="quotesearch">
            <div class="sltito">股票代码查询一览表：<a href="#sh">上海股票</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="#sz">深圳股票</a></div>
            <div class="sltit"><a name="sh"/>上海股票</div>

            <ul>
            <li><a target="_blank" href="http://quote.eastmoney.com/sh201000.html">R003(201000)</a></li>

            <li><a target="_blank" href="http://quote.eastmoney.com/sh201001.html">R007(201001)</a></li>

            <li><a target="_blank" href="http://quote.eastmoney.com/sh201002.html">R014(201002)</a></li>"""

# soup=gettestsoup()
stockurl="http://quote.eastmoney.com/sz002750.html"#目标股票地址
page =urllib.urlopen(stockurl)#用urllib获取网页
html1=page.read()#获取的网页数据保存到html1
html2 = open(unicode(str("123") + ".html", "utf-8"), "wb")#创建123的文本
html2.write(html1)#把html1内容写入html2
html2.close()
soup=getsoup(stockurl)#返回soup类型的数据，方便查询内容，因为我找的教程都是用BS提取的
x=soup.select(".cwzb")
#方法1
# print str(x)
# print str(soup.select(".cwzb")).decode('unicode_escape')
#方法2 其实不替换也不影响
y = str(x).replace('u\'','\'')
print y.decode("unicode-escape")

# for link in soup.find_all('a'):
#     print link.get_text(),
#     print(link.get('href'))

# print(link.get('href'))
# print soup.ul.li.get_text()
# print soup.select_one('html>body>div.qox>div.quotebody>div#quotesearch')
# print soup.text
# print soup.contents
