'''
tag name: we can locate the elements using tagname
         But tagname will consider the first occurance
syntax: driver.find_element('tag name','tagname_value')
'''
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(r'C:\Users\Jagadeesh Bandaru\PycharmProjects\selenium_training\files\css_selector_dup.html')
driver.find_element('tag name','input').send_keys('Ram')
time.sleep(2)
driver.find_element('tag name','input').send_keys('Ram@12345')

