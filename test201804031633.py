# coding:utf-8
from selenium import webdriver
import random
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys(u"测试部落")
driver.find_element_by_id("kw").submit()
s = driver.find_elements_by_css_selector("h3.t>a")
# 设置随机值
t = random.randint(0, 9)
# 随机取一个结果点击鼠标
s[t].click()