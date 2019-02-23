#!/usr/bin/python
#! encoding:utf-8
from bs4 import BeautifulSoup
import requests

# checkcity='jiangmen'
checkcity = 'abc'
find_checkcity = ''
pm25url = 'http://www.pm25.com/'
tempurl = pm25url + checkcity + '.html'
# print (tempurl) #test step
res = requests.get(tempurl)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, "lxml")
# if checkcity is not in the list, then checkcity will be assigned as bejing
for city1 in soup.select('.city_province_item'):
    for href1 in city1.select('a'):
        if checkcity in href1['href']:
            find_checkcity == 'yes'
if find_checkcity == '':
    find_checkcity = 'beijing'

# print(res.text)

# print (soup.text) #works
for city in soup.select('.banner_index'):
    mycity = city.select('h2')[0].text
    mypm25 = city.select('a')[2]['pm25']
    myqua = city.select('a')[2]['qua']
    print(mycity, ": 空气PM25-", mypm25, ", 空气质量-", myqua, )