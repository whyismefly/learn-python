# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup

import urllib.request
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

"""期间遇到了两个问题，第一个：
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
需要下载geckodriver，后面到https://github.com/mozilla/geckodriver/releases下载对应的版本后放到环境变量下的
目录中（python.exe位置那）即可解决。
后来下载后又出现
selenium.common.exceptions.WebDriverException: Message: Unable to find a matching set of capabilities.
期初以为是selenium与firefox版本不对应，后来更换了两个版本还是不行，折腾了半天发现需要把firefox的安装目录（
家里电脑不是默认安装路径）添加到环境变量中，最终解决了。累计前后折腾了4小时，大部分时间都花在龟速下载
geckodriver和错误路径的配置上，真是要命...
"""




"""获取验证码"""
# res = urllib.urlopen("http://www.baidu.com")
# print res.read()
# print "*"*150
# fp=webdriver.FirefoxProfile(r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\h35uyvpz.default')
# url = "http://www.labi.com/sms?type=1"
# x =webdriver.Firefox(fp)
# page=x.get(url)
# soup = BeautifulSoup(page,"html.parser")
# print soup

