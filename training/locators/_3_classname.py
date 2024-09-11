'''
class: whenever we are having class attribute we will go for class locator
class is not unique
syntax: driver.find_element('class name','classname_value')
'''


## Example 1 ##
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://demowebshop.tricentis.com/')
# driver.find_element('class name','ico-register').click()
# time.sleep(2)
# driver.find_element('class name','ico-login').click()
# time.sleep(2)
# driver.find_element('class name','cart-label').click()

## Example 2 ##
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://www.saucedemo.com/')
# # driver.find_element('class name','input_error form_input').send_keys('standard_user')
# # NoSuchElementExceptionye
# # only class name locator space should not be identified
# # so to overcome that issue space will be replaced with .
#
# driver.find_element('class name','input_error.form_input').send_keys('standard_user')
# time.sleep(1)

## Example 3 ##

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.find_element('class name','input_error.form_input').send_keys('standard_user')
time.sleep(2)
driver.find_element('class name','input_error.form_input').send_keys('secret_sauce')
time.sleep(2)
'''
whenever we are having with multiple elements with same locator and locator value
it will always consider the first occurence
so to avoid this drawback in the we can use any other locator inplace of class
'''
# in the above command,both username and password will be filled in username section only
















