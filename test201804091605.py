# coding:utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://mail.163.com/")
driver.implicitly_wait(30)
#切换iframe
driver.switch_to_frame("x-URS-iframe")
driver.find_element_by_name("email").send_keys("123")
driver.find_element_by_name("pssword").send_keys("456")