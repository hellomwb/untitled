# coding=utf-8
# 导入webdriver模块
from selenium import webdriver
import time
#导入键盘模块
from selenium.webdriver.common.keys import Keys
#打开浏览器
driver = webdriver.Chrome()
#打开工位系统
driver.get("http://192.168.203.112/")
driver.implicitly_wait(10)
h = driver.current_window_handle
print h
driver.find_element_by_xpath("//input[@class='ant-input inp mt28' and @type='text']").send_keys("admin@wafersystems.com")
driver.find_element_by_xpath("//input[@class='ant-input inp mt28' and @type='password']").send_keys("wafer123")
driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary' and @type='button']").click()
driver.find_element_by_xpath("//i[@class='iconfont icon-yidonggongwei' and @type='button']").click()

