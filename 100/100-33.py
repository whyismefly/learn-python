#!/usr/bin/python
# encoding:utf-8

# 题目：按逗号分隔列表。
# 程序分析：无。

list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

# print (str(n) for n in list)
# for n in list:
#     print n

douhao=','.join(str(n) for n in list)
print douhao

