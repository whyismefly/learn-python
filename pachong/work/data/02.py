#!/usr/bin/python
# encoding:utf-8

from abc import ABCMeta, abstractmethod
import re
import requests
import urllib
from bs4 import BeautifulSoup
import sys
sys.path.append("E:/GITHUBWORK/learn-python/pachong/stock")

def gethtmlbyurllib(url):
    page =urllib.urlopen(url)
    html=page.read()
    return html

def savehtml(html,savename):
    # html = open(str(savename)+".html", "wb")
    #中文会出现乱码
    html = open(unicode(str(savename) + ".html","utf-8"), "wb")
    try:
        html.write()
    finally:
        html.close()

def savehtmlastxt(html,savename):
    html = open(unicode(str(savename) + ".txt","utf-8"), "wb")
    try:
        html.write()
    finally:
        html.close()

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

textline = """</script>
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

url = "http://quote.eastmoney.com/stocklist.html"
# html=gethtmlbyurllib(url)
html=getsoup(url).contents
name = "汇总"
savehtml(html,name)

# soup=gettestsoup(html)
# for link in soup.find_all('a'):
#     print link.get_text(),
#     print(link.get('href'))

# print(link.get('href'))
# print soup.ul.li.get_text()
# print soup.select_one('html>body>div.qox>div.quotebody>div#quotesearch')
# print soup.text
# print soup.contents
