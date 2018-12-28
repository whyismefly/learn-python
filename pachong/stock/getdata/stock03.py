#!/usr/bin/python
# encoding:utf-8
# import requests


# URL = 'http://ip.taobao.com/service/getIpInfo.php'  # 淘宝IP地址库API
# try:
#     r = requests.get(URL, params={'ip': '8.8.8.8'}, timeout=1)
#     r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
# except requests.RequestException as e:
#     print(e)
# else:
#     result = r.json()
#     # print(type(result), result, sep='\n')#这是python3的写法...
#     print type(result), result, '\n'
import re
import requests
import bs4
from bs4 import BeautifulSoup
import sys
sys.path.append("E:/GITHUBWORK/learn-python/pachong/stock")

url="http://quote.eastmoney.com/stocklist.html"
req=requests.get(url)
soup=BeautifulSoup(req.content,"lxml")

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

# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
searchObj = re.search(r'target.*', soup, re.M | re.I)

if searchObj:
    print "searchObj.group() : ", searchObj.group()
else:
    print "No search!!"


