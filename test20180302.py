# coding=utf-8
# 导入webdriver模块
from selenium import webdriver
#打开浏览器
driver = webdriver.Chrome()
#打开工位系统
driver.get("http://xa.ganji.com/")
driver.implicitly_wait(10)
#获取当前窗口句柄
h=driver.current_window_handle
print h
driver.find_element_by_link_text("全职").click()
all_h=driver.window_handles
print all_h
driver.switch_to.window(all_h[1])
print driver.title