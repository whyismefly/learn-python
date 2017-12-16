# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        # self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.labi.com/login?backUrl=%2Fsms%3Ftype%3D1")
        driver.find_element_by_id("mlog_un").click()
        driver.find_element_by_id("mlog_un").clear()
        driver.find_element_by_id("mlog_un").send_keys("ftxsb")
        driver.find_element_by_id("mlog_pwd").click()
        driver.find_element_by_id("mlog_pwd").clear()
        driver.find_element_by_id("mlog_pwd").send_keys("xiaoshoubu")
        driver.find_element_by_xpath("//a[@id='btnLogin']/span").click()
        # driver.find_element_by_xpath("//body").click()
        # driver.find_element_by_id("mlog_ck").click()
        # driver.find_element_by_id("pp_lw_m").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
