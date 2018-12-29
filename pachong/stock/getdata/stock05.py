#!/usr/bin/python
# encoding:utf-8

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


# # matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
# searchObj = re.search(r'target.*', line, re.M | re.I)
#
# if searchObj:
#     print "searchObj.group() : ", searchObj.group()
# else:
#     print "No search!!"