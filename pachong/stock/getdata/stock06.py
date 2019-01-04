#!/usr/bin/python
# encoding:utf-8
import bs4
from bs4 import BeautifulSoup
import requests

html = """ 2 <html><head><title>The Dormouse's story</title></head>
 3 <body>
 4 <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
 5 <p class="story">Once upon a time there were three little sisters; and their names were
 6 <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
 7 <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
 8 <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
 9 and they lived at the bottom of a well.</p>
10 <p class="story">...</p>
"""
<<<<<<< HEAD


class Info():
    def info(self):
        return "testInfo"

    def getstockinfo(soup):
        for link in soup.find_all('a'):
            return link.get_text(),(link.get('href'))
            print link.get_text(),(link.get('href'))

soup = BeautifulSoup(html, "lxml")
x=Info.getstockinfo(soup)
=======
soup = BeautifulSoup(html,"lxml")
for link in soup.find_all('a'):
    print(link.get('href'))
>>>>>>> 0703c8d3131241f6455dbdf276ae37b2b6f98eaf
