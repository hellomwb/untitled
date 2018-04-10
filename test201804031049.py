# coding:utf-8
import random
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys(u"测试部落")
driver.find_element_by_id("kw").submit()
s = driver.find_elements_by_css_selector("h3.t>a")
for i in s:
    print i.get_attribute("href")
t=random.randint(0,9)
a=s[t].get_attribute("href")
print(a)
driver.implicitly_wait(10)
driver.get(a)