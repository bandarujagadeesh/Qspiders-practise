'''
name: whenever we are having id attribute we will go for id locator
name is not unique
syntax: driver.find_element('name','name_value)
'''
## Example 1 ##
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://www.instagram.com/')
# driver.find_element('name','username').send_keys('Ram')
# time.sleep(2)
# driver.find_element('name','password').send_keys('Ramiyodya')
# time.sleep(2)

## Example 2 ##
import time
from  selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options = options)
driver.get('https://www.saucedemo.com/')
driver.find_element('name','user-name').send_keys('standard_user')
time.sleep(2)
driver.find_element('name','password').send_keys('secret_sauce')
time.sleep(2)
driver.find_element('name','login-button').click()

