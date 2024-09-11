'''
partial link text:link text is present in between the anchor tag we call it as link text
if we took halfname if it is too long
* to avoid unwanted spaces we use partial link text for example - 'Books    '
* to avoid large text we use partial link text for example - 'home & kitchen'

syntax: driver.find_element('partial link text','value')
'''
# ## Example 1 ##
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
# driver.find_element('partial link text','Reg').click()
# time.sleep(2)
# driver.find_element('partial link text','Log').click()
# time.sleep(2)
# driver.find_element('partial link text','Books').click()
# time.sleep(2)
# driver.find_element('partial link text','Apparel & Shoes').click()

## Example 2 ##
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.shoppersstack.com/')
time.sleep(6)
driver.find_element('partial link text','B').click()
time.sleep(2)
