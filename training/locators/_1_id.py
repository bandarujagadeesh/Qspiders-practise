'''
id: whenever we are having id attribute we will go for id locator
id is unique
syntax: driver.find_element('id','id_value)
'''

## Example 1 ##
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://www.saucedemo.com/')
# driver.find_element('id','user-name').send_keys('standard_user')
# time.sleep(2)
# driver.find_element('id','password').send_keys('secret_sauce')
# time.sleep(2)
# driver.find_element('id','login-button').click()
# time.sleep(2)
# driver.find_element('id','react-burger-menu-btn').click()
# time.sleep(2)
# driver.find_element('id','logout_sidebar_link').click()

## Example 2 ##

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.find_element('id','name').send_keys('Ram')
time.sleep(2)
driver.find_element('id','email').send_keys('Ram@iyodya.com')
time.sleep(2)
driver.find_element('id','phone').send_keys('9014704235')
time.sleep(2)
driver.find_element('id','textarea').send_keys('Iyodya')