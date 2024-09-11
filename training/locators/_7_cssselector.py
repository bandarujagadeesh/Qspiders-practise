'''
css selector : to locate the web-elements using any attribute name and attribute value, we go for css selector
syntax: tagname[attribute_name='attribute_value']

Drawbacks
1. indexing is not possible,whenever we have multiple occurances, css selector will always consider first occurance
2.locating text is not possible in css_selector
3.back traversing is not possible in css selector
'''

## Example 1 ##
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://www.facebook.com/signup')
# time.sleep(2)
# driver.find_element('css selector','input[aria-label="First name"]').send_keys('jaggu')
# time.sleep(2)
# driver.find_element('css selector','input[aria-label="Surname"]').send_keys('kummu')
# time.sleep(2)
# driver.find_element('css selector','input[aria-label="Mobile number or email address"]').send_keys('9030590231')
# time.sleep(2)
# driver.find_element('css selector','input[autocomplete="new-password"]').send_keys('jaggu143kummu')

## Example 2 ##
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
# driver.find_element('css selector','input[data-test="username"]').send_keys('standard_user')
# time.sleep(2)
# driver.find_element('css selector','input[data-test="password"]').send_keys('secret_sauce')
# time.sleep(2)
# driver.find_element('css selector','input[data-test="login-button"]').click()
# time.sleep(2)
# driver.find_element('css selector','button[id="react-burger-menu-btn"]').click()
# time.sleep(2)
# driver.find_element('css selector','a[id="logout_sidebar_link"]').click()

## Example 3 ##
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
# driver.find_element('css selector','a[class="ico-register"]').click()
# time.sleep(2)
# driver.find_element('css selector','a[class="ico-login"]').click()

## Example 4 ##
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
time.sleep(2)
driver.find_element('css selector','input[class="input_error form_input"]').send_keys('standard_user')
time.sleep(2)
driver.find_element('css selector','input[class="input_error form_input"]').send_keys('secret_sauce')

## issue css_selector will always consider first occuerance as he have same attribute name and attribute value
