# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


# class Login2(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.base_url = "http://www.baidu.com/"
#         self.verificationErrors = []
#         self.accept_next_alert = True
#
#     def test_login2(self):
#         driver = self.driver
#         driver.get(
#             "http://134.64.106.187:8000/sso/login?service=http%3A%2F%2F134.64.106.187"
#             "%3A8000%2Fportal%2FhomePage%21initHomePage.action%"
#             "3BManaged_Server_Name%3D134.64.117.183%3A9001")
#         # driver.find_element_by_id("main").click()
#         # driver.find_element_by_id("main").click()
#         # driver.find_element_by_id("username").click()
#         # driver.find_element_by_id("username").click()
#         driver.find_element_by_id("username").clear()
#         driver.find_element_by_id("username").send_keys("920214")
#         # driver.find_element_by_id("main").click()
#         # driver.find_element_by_id("password").click()
#         driver.find_element_by_id("password").clear()
#         driver.find_element_by_id("password").send_keys("Ft123456")
#         # driver.find_element_by_id("main").click()
#         driver.find_element_by_id("msgsid").click()
#         # driver.find_element_by_id("smscode").click()
#         driver.find_element_by_id("smscode").clear()
#         driver.find_element_by_id("smscode").send_keys("1948")
#         driver.find_element_by_id("submit").click()
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


def test_login2(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

        driver = self.driver
        driver.get(
            "http://134.64.106.187:8000/sso/login?service=http%3A%2F%2F134.64.106.187"
            "%3A8000%2Fportal%2FhomePage%21initHomePage.action%"
            "3BManaged_Server_Name%3D134.64.117.183%3A9001")
        # driver.find_element_by_id("main").click()
        # driver.find_element_by_id("main").click()
        # driver.find_element_by_id("username").click()
        # driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("920214")
        # driver.find_element_by_id("main").click()
        # driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("Ft123456")
        # driver.find_element_by_id("main").click()
        driver.find_element_by_id("msgsid").click()
        # driver.find_element_by_id("smscode").click()
        driver.find_element_by_id("smscode").clear()
        driver.find_element_by_id("smscode").send_keys("1948")
        driver.find_element_by_id("submit").click()

print test_login2