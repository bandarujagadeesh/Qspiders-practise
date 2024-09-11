'''
1.  wap to fetch the name and price of adidas original shoes in Myntra.com. Output should look like
    shoe name - Price
2.  wap to print all the available colors for adidas original shoes in Myntra.com
3.  wap to fetch the names of the recommended movies in bookmyshow
4.  Go to https://www.qspiders.com/, click on courses, wap to print all the courses available
5.  Wap to fetch all the dishes available in any restraunt in zomato.com

'''

# wap to fetch the name and price of adidas original shoes in Myntra.com. Output should look like shoe name - Price
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.myntra.com/')
# time.sleep(3)
# driver.find_element('css selector','input[placeholder="Search for products, brands and more"]').send_keys('adidas original shoes')
# time.sleep(2)
# driver.find_element('xpath','//li[text()="Adidas Original Shoes"]').click()
# time.sleep(2)
# shoe_names = driver.find_elements('xpath','//ul[@class="results-base"]//h4[@class="product-product"]')
# prices = driver.find_elements('xpath','//ul[@class="results-base"]//div[@class="product-price"]')
# shoes_list = [shoe_name.text for shoe_name in shoe_names]
# price_list = [price.text for price in prices]
# for shoe,price in zip(shoes_list,price_list):
#     print(f'{shoe} - {price}')

# wap to print all the available colors for adidas original shoes in Myntra.com
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.myntra.com/')
# time.sleep(3)
# driver.find_element('css selector','input[placeholder="Search for products, brands and more"]').send_keys('adidas original shoes')
# time.sleep(2)
# driver.find_element('xpath','//li[text()="Adidas Original Shoes"]').click()
# time.sleep(2)
# click_colour_more =  driver.find_element('class name','colour-more').click()
# time.sleep(2)
# all_colours = driver.find_elements('xpath','(//div[@class="vertical-filters-filters"])[2]//li//label')
# for colour in all_colours:
#     print(colour.text)

# wap to fetch the names of the recommended movies in bookmyshow
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://in.bookmyshow.com/')
# time.sleep(2)
# driver.find_element('xpath','//input[@placeholder="Search for your city"]').send_keys('Hyderabad')
# time.sleep(2)
# driver.find_element('xpath','//strong[text()="Hyderabad"]').click()
# time.sleep(2)
# recommended_movies_see_all = driver.find_element('xpath','(//div[text()="See All ›"])[1]')
# recommended_movies_see_all.click()
# time.sleep(2)
# movie_names = driver.find_elements('xpath','//div[@class="sc-b1h692-8 cnOKlF"]//div[@class="sc-7o7nez-0 hGuczM"]')
# for movie_name in movie_names:
#     print(movie_name.text)

# Go to https://www.qspiders.com/, click on courses, wap to print all the courses available
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.qspiders.com/')
# time.sleep(2)
# driver.find_element('xpath','//a[@class="navbar-item"]//span[text()="Courses"]').click()
# time.sleep(2)
# course_names = driver.find_elements('xpath','//div[@class="columns is-multiline"]//p')
# for course_name in course_names:
#     print(course_name.text)

# Wap to fetch all the dishes available in any restraunt in zomato.com
import time
from selenium import webdriver
from selenium.webdriver import Keys

driver = webdriver.Firefox()
driver.get('https://www.zomato.com/')
time.sleep(2)
driver.find_element('xpath','//input[@placeholder="Hyderabad"]').send_keys('Hyderabad')
time.sleep(2)
driver.find_element('xpath','//input[@placeholder="Search for restaurant, cuisine or a dish"]').send_keys('Pizza Hut')
time.sleep(1)
driver.find_element('xpath','//input[@placeholder="Search for restaurant, cuisine or a dish"]').click()
time.sleep(5)
restaurant_link = driver.find_element('xpath', '//a[contains(@href, "pizza-hut") and contains(@class, "result-title")]')
restaurant_link.click()
time.sleep(10)

