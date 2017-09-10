#!/usr/bin/python
# encoding:utf-8
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

# def getImg(html):
#     reg = r'src="(.+?\.jpg)" pic_ext'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre,html)
#     x = 0
#     for imgurl in imglist:
#         urllib.urlretrieve(imgurl,'%s.jpg' % x)
#         x+=1

# print getImg(html)

m110="http://www.apta.gov.cn/Officer/Summary?examid=64&&pcode=&pi=4"
m150="http://www.apta.gov.cn/Officer/Summary?examid=64&&pcode=&pi=5"
m520="http://www.apta.gov.cn/Officer/Summary?examid=64&&pcode=&pi=12"

h110=getHtml(m110)
h150=getHtml(m150)
h520=getHtml(m520)


print h110,h150,h520
