# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

"""加载cookie"""
# fp=webdriver.FirefoxProfile(r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles')
fp=webdriver.FirefoxProfile(r'C:\Users\WHY-LENGEND\AppData\Roaming\Mozilla\Firefox\Profiles\1qatadyp.default')

driver=webdriver.Firefox(fp)
driver.maximize_window()

"""打开EDP"""
# driver.get("http://134.64.106.187:8000/sso/login?service=http%3A%2F%2F134.64.106.187"
#             "%3A8000%2Fportal%2FhomePage%21initHomePage.action%"
#             "3BManaged_Server_Name%3D134.64.117.183%3A9001")
#
# driver.find_element_by_id("username").clear()
# driver.find_element_by_id("username").send_keys("920214")
# driver.find_element_by_id("password").clear()
# driver.find_element_by_id("password").send_keys("Ft123456")
# driver.find_element_by_id("msgsid").click()


"""打开蜡笔"""
driver.get("http://www.labi.com/sms?type=1")
driver.find_element_by_id("mlog_un").clear()
driver.find_element_by_id("mlog_un").send_keys("ftxsb")
driver.find_element_by_id("mlog_pwd").clear()
driver.find_element_by_id("mlog_pwd").send_keys("xiaoshoubu")
driver.find_element_by_id("btnLogin").click()


# js='window.open("http://www.labi.com/sms?type=1");'
# driver.execute_script(js)
# driver.find_element_by_id("mlog_un").clear()
# driver.find_element_by_id("mlog_un").send_keys("ftxsb")
# driver.find_element_by_id("mlog_pwd").clear()
# driver.find_element_by_id("mlog_pwd").send_keys("xiaoshoubu")
# driver.find_element_by_id("mlog_ck").click()



"""获取验证码"""

#
# driver.find_element_by_id("smscode").clear()
# driver.find_element_by_id("smscode").send_keys("1948")
# driver.find_element_by_id("submit").click()