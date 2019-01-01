#!/usr/bin/python
# encoding:utf-8

import re
import requests
import bs4
from bs4 import BeautifulSoup
import sys
sys.path.append("E:/GITHUBWORK/learn-python/pachong/stock")

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

soup=gettestsoup()
print soup.select_one('html>body>div.qox>div.quotebody>div#quotesearch')
# print soup.text
# print soup.contents
