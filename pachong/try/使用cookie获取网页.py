#!usr/bin/python
# encoding:utf-8
import requests
from bs4 import BeautifulSoup
url="http://www.baidu.com/"
cookie={"BDUSS":
        "pyaVhZbE0yNDFzRmV1TlhnWTBVWWF2SVczcE0zd2hFVVNyY2NHeDE3T042bUpjQVFBQUFBJCQAAAAAAAAAAAEAAAD8SIsHd2h5aXNtZWZs"
        "eQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI1dO1yNXTtcOG"
}
req=requests.get(url,cookies=cookie)
soup=BeautifulSoup(req.content,"lxml")
print soup
#写法一
# with open("baidu.html","wb") as file:
#     file.write(soup.encode("utf-8"))
#     file.close()

#写法二
# html1 = open( "baidu1.html", "wb")
# html1.write(soup.encode("utf-8"))
# html1.close()
