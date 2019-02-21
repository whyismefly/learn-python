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
with open("baidu.html","wb") as file:
    file.write(soup.encode("utf-8"))
    file.close()
