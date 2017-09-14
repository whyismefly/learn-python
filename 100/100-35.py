#!/usr/bin/python
# encoding:utf-8

# 题目：文本颜色设置。
# 程序分析：无。

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC

print bcolors.HEADER + "警告的颜色字体?"
print bcolors.OKBLUE + "警告的颜色字体?"
print bcolors.OKGREEN + "警告的颜色字体?"
print bcolors.WARNING + "警告的颜色字体?"
print bcolors.FAIL + "警告的颜色字体?"
print bcolors.ENDC + "警告的颜色字体?"
print bcolors.BOLD + "警告的颜色字体?"
print bcolors.UNDERLINE + "警告的颜色字体?"
print bcolors.UNDERLINE + "警告的颜色字体?" + bcolors.OKBLUE+"3423RT34Y65Y65"
