# coding=utf-8
#导入webdriver模块
from selenium import webdriver
import time
#打开浏览器
driver = webdriver.Chrome()
#打开百度
driver.get("http://www.baidu.com")
#设置休眠时间
time.sleep(3)
print (driver.title)
driver.get('https://testerhome.com/')
time.sleep(3)
driver.refresh()
driver.back()
time.sleep(3)
driver.forward()
print (driver.title)
#设置浏览器大小
driver.set_window_size(540,960)
time.sleep(2)
driver.maximize_window()
driver.get_screenshot_as_file('D:\\image\\n.png')
driver.close()
