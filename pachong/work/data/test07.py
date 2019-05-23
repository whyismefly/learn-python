# !/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import urllib
from bs4 import BeautifulSoup
import pandas
import cookielib

"""
Request URL: http://134.64.116.90:8030/sdp/p1521813509851_AutoCreateZul_207.zul
Request Method: GET
Status Code: 200 OK
Remote Address: 134.64.116.90:8030
Referrer Policy: no-referrer-when-downgrade
Cache-Control: no-cache
Cache-Control: no-store
Connection: close
Content-Encoding: gzip
Content-Language: zh-CN
Content-Length: 6322
Content-Type: text/html;charset=UTF-8
Date: Thu, 09 May 2019 00:14:57 GMT
Expires: -1
Pragma: no-cache
Server: Microsoft-IIS/8.5
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: JSESSIONID=C94E008A4B155EDD9072D952DE1A6F7D; Managed_Server_Name="134.64.70.57:8020"; PHPSESSID=7d52ff757b92; JSESSIONID-LDC=n4yhcTvCJDTZ3n6HbSXGgjWP7h8vVNmhTPnZGFLklkZhPdMWRYH1!560399883
Host: 134.64.116.90:8030
Referer: http://134.64.116.90:9185/ldc/home.jsp;jsessionid=n4yhcTvCJDTZ3n6HbSXGgjWP7h8vVNmhTPnZGFLklkZhPdMWRYH1!560399883!1557360578627
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36
"""


"""
LOGIN_URL = 'http://yingxiao.chewumi.com/login.php'  #请求的URL地址
DATA = {"username":'accountID',"passwd":'passwd'}   #登录系统的账号密码,也是我们请求数据

HEADERS = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' #模拟登陆的浏览器
           }
RES = requests.post(LOGIN_URL,data=DATA,headers=HEADERS)  #模拟登陆操作
print (RES.text) #打印返回的文本信息
"""


LOGIN_URL="http://134.64.116.90:8030/sdp/p1521813509851_AutoCreateZul_207.zul;Managed_Server_Name=134.64.70.56:8020"
Cookies="""JSESSIONID=F3A178815DBA239BA7C2397D55E238D3; Managed_Server_Name="134.64.70.56:8020"; PHPSESSID=7d52ff757b92; BIGipServerpool_nbtyrz1=544489606.28451.0000; jsessionid_zHSp=Orjekdq5gUoGYlUPh4mE8TPZRUYWz59Uq193nhvS53n25Zpk1Yts!-791586314; PORTAL_SID=rvBXcldDp41hFjMcmjdfkMQFvJkk5J3YjrhdDNgTGWJFhfmsh6Nb!-723442693; IDEALSEARCH_AH=0xylcmPNZyt3pllnWQ94Rs7NvWQGGw62L8qv81cvy2HSyY2XvZf6!961753984; JSESSIONID-LDC=n22bcmVW5JLGxCyVl1Q7S1MvN9lSJsLlGk4fpTSTN5z7CJHB1GpM!560399883; JSESSIONID=8zDZcmFdCZ7hkHDhzxvhr1mhMRqGQlwR23QhRhfmRH2vKxpcWQyQ!120989381"""
Cookie={'JSESSIONID':'F3A178815DBA239BA7C2397D55E238D3',
        ' Managed_Server_Name':"134.64.70.56:8020",
        'PHPSESSID':'7d52ff757b92',
        'BIGipServerpool_nbtyrz1':'544489606.28451.0000',
        'jsessionid_zHSp':'Orjekdq5gUoGYlUPh4mE8TPZRUYWz59Uq193nhvS53n25Zpk1Yts!-791586314',
        'PORTAL_SID':'rvBXcldDp41hFjMcmjdfkMQFvJkk5J3YjrhdDNgTGWJFhfmsh6Nb!-723442693',
        'IDEALSEARCH_AH':'0xylcmPNZyt3pllnWQ94Rs7NvWQGGw62L8qv81cvy2HSyY2XvZf6!961753984',
        'JSESSIONID-LDC':'n22bcmVW5JLGxCyVl1Q7S1MvN9lSJsLlGk4fpTSTN5z7CJHB1GpM!560399883',
        'JSESSIONID':'8zDZcmFdCZ7hkHDhzxvhr1mhMRqGQlwR23QhRhfmRH2vKxpcWQyQ!120989381"'}
# RequestHeaders={Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Encoding:gzip, deflate
# Accept-Language:zh-CN,zh;q=0.9
# Cache-Control:max-age=0
# Connection:keep-alive
# Cookie:JSESSIONID=F3A178815DBA239BA7C2397D55E238D3; Managed_Server_Name="134.64.70.56:8020"; PHPSESSID=7d52ff757b92; BIGipServerpool_nbtyrz1=544489606.28451.0000; jsessionid_zHSp=Orjekdq5gUoGYlUPh4mE8TPZRUYWz59Uq193nhvS53n25Zpk1Yts!-791586314; PORTAL_SID=rvBXcldDp41hFjMcmjdfkMQFvJkk5J3YjrhdDNgTGWJFhfmsh6Nb!-723442693; IDEALSEARCH_AH=0xylcmPNZyt3pllnWQ94Rs7NvWQGGw62L8qv81cvy2HSyY2XvZf6!961753984; JSESSIONID-LDC=n22bcmVW5JLGxCyVl1Q7S1MvN9lSJsLlGk4fpTSTN5z7CJHB1GpM!560399883; JSESSIONID=8zDZcmFdCZ7hkHDhzxvhr1mhMRqGQlwR23QhRhfmRH2vKxpcWQyQ!120989381
# Host:134.64.116.90:8030
# Referer:http://134.64.116.90:9185/ldc/home.jsp
# Upgrade-Insecure-Requests:1
# User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36}
req=requests.get(LOGIN_URL,cookies=Cookie)
# print req.cookies
# print type(req.cookies)
print req.text
# print Cookies