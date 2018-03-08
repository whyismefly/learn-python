# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
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


"""加载cookie"""
fp=webdriver.FirefoxProfile(r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\h35uyvpz.default')
# fp=webdriver.FirefoxProfile(r'C:\Users\WHY-LENGEND\AppData\Roaming\Mozilla\Firefox\Profiles\1qatadyp.default')
driver=webdriver.Firefox(fp)
# driver.maximize_window()

# handles = driver.window_handles
# driver.switch_to_window(handles[0])
# handles = driver.window_handles
# driver.switch_to_window(handles[-1])


"""打开EDP"""
def  GetEdp():
    driver.get("http://134.64.106.187:8000/sso/login?service=http%3A%2F%2F134.64.106.187"
            "%3A8000%2Fportal%2FhomePage%21initHomePage.action%"
            "3BManaged_Server_Name%3D134.64.117.183%3A9001")
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("920214")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("Ft123456")
    driver.find_element_by_id("msgsid").click()

def  GetEdp(user,password):
    driver.get("http://134.64.106.187:8000/sso/login?service=http%3A%2F%2F134.64.106.187"
            "%3A8000%2Fportal%2FhomePage%21initHomePage.action%"
            "3BManaged_Server_Name%3D134.64.117.183%3A9001")
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(user)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("msgsid").click()

def  GetEdp(url,user,password):
    driver.get(url)
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(user)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("msgsid").click()


"""打开蜡笔"""
def  GetLabi():
    driver.get("http://www.labi.com/sms?type=1")
    # driver.find_element_by_id("mlog_un").clear()
    # driver.find_element_by_id("mlog_un").send_keys("ftxsb")
    # driver.find_element_by_id("mlog_pwd").clear()
    # driver.find_element_by_id("mlog_pwd").send_keys("xiaoshoubu")
    # driver.find_element_by_id("btnLogin").click()

def  GetLabi2():
    driver.get("http://www.labi.com/sms?type=1")
    driver.find_element_by_id("mlog_un").clear()
    driver.find_element_by_id("mlog_un").send_keys("ftxsb")
    driver.find_element_by_id("mlog_pwd").clear()
    driver.find_element_by_id("mlog_pwd").send_keys("xiaoshoubu")
    driver.find_element_by_id("btnLogin").click()

def  GetLabi(user,password):
    driver.get("http://www.labi.com/sms?type=1")
    driver.find_element_by_id("mlog_un").clear()
    driver.find_element_by_id("mlog_un").send_keys(user)
    driver.find_element_by_id("mlog_pwd").clear()
    driver.find_element_by_id("mlog_pwd").send_keys(password)
    driver.find_element_by_id("btnLogin").click()


"""获取验证码"""
res = urllib.urlopen("http://www.baidu.com")
print res.read()
print "*"*150
url = "http://www.sohu.com/"
page = urllib.urlopen(url)
soup = BeautifulSoup(page,"html.parser")
print soup


"""输入验证码verification """


# driver.find_element_by_id("smscode").clear()
# driver.find_element_by_id("smscode").send_keys("1948")
# driver.find_element_by_id("submit").click()




"""取四级实时战报"""
driver.get("http://134.64.106.187:8000/sso/login?service=http%3A%2F%2F134.64.106.187"
            "%3A8000%2Fportal%2FhomePage%21initHomePage.action%"
            "3BManaged_Server_Name%3D134.64.117.183%3A9001")
# driver.get("http://134.64.116.90:9116/FocusDay/"
#            "Direct.jsp?ApplicationResponse=554&EmployeeId=920214&"
#            "TypeID=1&fromPortal=1&lastMenuCode=122521601")

# driver = self.driver
# driver.get(
#     "http://134.64.106.187:8000/sso/login?service=http%3A%2F%2F134.64.106.187%3A8000%2Fportal%2FhomePage
# %21initHomePage.action%3BManaged_Server_Name%3D134.64.117.183%3A9001")
# driver.find_element_by_id("username").click()
# driver.find_element_by_id("password").clear()
# driver.find_element_by_id("password").send_keys("Ft123456")
# driver.find_element_by_id("username").clear()
# driver.find_element_by_id("username").send_keys("920214")
# driver.find_element_by_id("msgsid").click()
# driver.find_element_by_id("smsgetmsg").click()
# driver.find_element_by_id("smscode").click()
# driver.find_element_by_id("smscode").clear()
# driver.find_element_by_id("smscode").send_keys("5241")
# driver.find_element_by_id("submit").click()
# # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=6 | ]]
# driver.find_element_by_link_text(u"实时战报").click()
# # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
# driver.find_element_by_link_text(u"四级实时战报").click()
# driver.find_element_by_id("searchStartDayId").click()
# # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
# driver.find_element_by_xpath("//td[@onclick='day_Click(2017,12,16);']").click()
# # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
# driver.find_element_by_id("searchStartDayId").clear()
# driver.find_element_by_id("searchStartDayId").send_keys("20171216")
# driver.find_element_by_id("searchEndDayId").click()
# # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
# driver.find_element_by_xpath("//td[@onclick='day_Click(2017,12,16);']").click()
# # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
# driver.find_element_by_id("searchEndDayId").clear()
# driver.find_element_by_id("searchEndDayId").send_keys("20171216")
# driver.find_element_by_name("reportSearch").click()
# driver.find_element_by_name("reportSearch").click()
# driver.find_element_by_name("reportExport").click()
# driver.find_element_by_id("yzmBtn").click()
# driver.find_element_by_id("code").click()
# driver.find_element_by_id("code").clear()
# driver.find_element_by_id("code").send_keys("263913")
# driver.find_element_by_xpath(u"//input[@value='确认']").click()

#数据中心数据
# http://134.64.116.90:9185/ldc/home.jsp

# driver.get(
#     "http://134.64.106.187:8000/portal/homePage!initHomePage.action;jsessionid=
# r5RVh2QRp8xv9Mr0h4K1G2qLBvbKz5mX7sDt2gGwZyY6h5qM2Bsb!-1399182646")
# # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=6 | ]]
# driver.find_element_by_link_text(u"实时战报").click()
# # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
# driver.find_element_by_link_text(u"四级实时战报").click()