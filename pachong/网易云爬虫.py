from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get('http://detail.tmall.com/item.htm?id=12577759834 ')
time.sleep(10)
pageSource = browser.page_source
print pageSource
browser.close()