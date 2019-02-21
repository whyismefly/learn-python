#!usr/bin/python
# encoding:utf-8
import requests
from bs4 import BeautifulSoup

#百度登录
url="http://www.baidu.com/"
cookie={"BDUSS":
        "pyaVhZbE0yNDFzRmV1TlhnWTBVWWF2SVczcE0zd2hFVVNyY2NHeDE3T042bUpjQVFBQUFBJCQAAAAAAAAAAAEAAAD8SIsHd2h5aXNtZWZs"
        "eQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI1dO1yNXTtcOG"
}
# req=requests.get(url,cookies=cookie)
# soup=BeautifulSoup(req.content,"lxml")
# print soup
#写法一
# with open("baidu.html","wb") as file:
#     file.write(soup.encode("utf-8"))
#     file.close()

#写法二
# html1 = open( "baidu1.html", "wb")
# html1.write(soup.encode("utf-8"))
# html1.close()

#内网登录

url1="http://134.64.116.90:8081/?mscg-ip=134.64.50.241"
cookie1={"PHPSESSID":
        "7d52ff757b92"
}
req1=requests.get(url1,cookies=cookie1)
soup1=BeautifulSoup(req1.content,"lxml")
print soup1
html1 = open( "test.html", "wb")
html1.write(soup1.encode("utf-8"))
html1.close()