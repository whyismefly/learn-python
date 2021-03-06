#!/usr/bin/python
# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, retest
import os,sys,retest
import subprocess

#网络状态检测
def NetCheck(ip):
   try:
    p = subprocess.Popen(["ping -c 1 -w 1 "+ ip],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    out=p.stdout.read()
    #err=p.stderr.read()
    regex=retest.compile('100% packet loss')
    #print out
    #print regex
    #print err
    if len(regex.findall(out)) == 0:
        print ip + ': host up'
        return 'UP'
    else:
        print ip + ': host down'
        return 'DOWN'
   except:
    print 'NetCheck work error!'
    return 'ERR'
if __name__ == '__main__':
    NetCheck('10.20.0.56')
    NetCheck('10.10.0.56')
    NetCheck('10.10.0')


# #网络登录
# class Login(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.base_url = "http://134.64.116.90:8081/"
#         self.verificationErrors = []
#         self.accept_next_alert = True
#
#     def test_1(self):
#         driver = self.driver
#         driver.get(self.base_url + "/?mscg-ip=134.64.50.241")
#         # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | mainFrame | ]]
#         driver.find_element_by_id("PassWord").clear()
#         driver.find_element_by_id("PassWord").send_keys("why12345")
#         driver.find_element_by_id("UserName").clear()
#         driver.find_element_by_id("UserName").send_keys("146837")
#         driver.find_element_by_id("loginbutton1").click()
#
#     def is_element_present(self, how, what):
#         try:
#             self.driver.find_element(by=how, value=what)
#         except NoSuchElementException as e:
#             return False
#         return True
#
#     def is_alert_present(self):
#         try:
#             self.driver.switch_to_alert()
#         except NoAlertPresentException as e:
#             return False
#         return True
#
#     def close_alert_and_get_its_text(self):
#         try:
#             alert = self.driver.switch_to_alert()
#             alert_text = alert.text
#             if self.accept_next_alert:
#                 alert.accept()
#             else:
#                 alert.dismiss()
#             return alert_text
#         finally:
#             self.accept_next_alert = True
#
#     def tearDown(self):
#         self.driver.quit()
#         self.assertEqual([], self.verificationErrors)
#
#
# if __name__ == "__main__":
#     unittest.main()
