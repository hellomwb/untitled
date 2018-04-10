# coding=utf-8
#导入webdriver模块
from selenium import webdriver
import time
#打开浏览器
driver = webdriver.Chrome()
#打开百度
driver.get("http://www.baidu.com")
# driver.find_element_by_id('kw').send_keys('python')
# driver.find_element_by_id('su').click()
# time.sleep(2)
# driver.find_element_by_id('kw').clear()
# driver.find_element_by_name('wd').send_keys('java')
# driver.find_element_by_id('su').click()
#driver.find_element_by_link_text('hao123').click()
driver.find_element_by_xpath(".//*[@id='kw']").send_keys("python")
driver.find_element_by_id('su').click()
time.sleep(2)
driver.find_element_by_id('kw').clear()
driver.find_element_by_css_selector("[name='wd']").send_keys(u"孟武斌")
driver.find_element_by_id('kw').submit()
print (driver.title)