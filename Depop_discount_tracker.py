#Import libraries
import os
import selenium
from selenium import webdriver
import time
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


'''
Inststalls the chromedriver & opens up a chrome new window
'''
service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service = service)


'''
Specifies the url being used and opens it in the new chrome window

Args:
    driver.get() (method) = navigate to a page given by the URL
'''
qurl = "https://www.depop.com/explore"
driver.get(qurl.format(sort='relevance'))


'''
Scrolls to the end of the page multiple times to load in more products

Args:
    driver.execute_script() (method) = executes JavaScript commands
    time.sleep() (method) = suspends the execution of code for a number of seconds
'''
#Scroll to the end of the page multiple times
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)  


'''
Searching through HTML tags to return a list of discount prices

Args:
    driver.find_elements() (method) = returns a list of objects of the type WebElement
    prices.append() (method) = adds an element to the end of a list
    price.get_attribute() (method) = returns the value of a specified attribute in the element
'''

discount_prices = driver.find_elements(by=By.XPATH, value = "//p[contains(@class,'jIdiRl')]")
prices = []
for i in range(0,len(discount_prices)):
    price = discount_prices[i]
    prices.append(price.get_attribute("innerHTML"))
    print(price.get_attribute("innerHTML"))


'''
Iterate through li tags to get item name

Args:
    driver.find_elements() (method) = returns a list of objects of the type WebElement
    item.find_elements() (method) = returns a list of objects of the type WebElement
    dcnt_prices[j].get_attribute() (method) = returns the value of a specified attribute in the element
    discount_prices_list.append() (method) = adds an element to the end of a list
    item_name_list.append() (method) = adds an element to the end of a list
'''
listed_items = driver.find_elements(by=By.XPATH, value="//li[contains(@class,'cAJcNu')]")

item_name_list = []
discount_prices_list = []

# loop over list of items found to get other elements contained within
for i in range(0, len(listed_items)):
    item = listed_items[i]
    
    #find discounted price in list container
    dcnt_prices = item.find_elements(by=By.XPATH, value=".//p[contains(@class,'jIdiRl')]")
    
    #find item description from anchor href attribute
    item_name = item.find_elements(by=By.XPATH, value=".//a[contains(@class,'htETKn')]") #.get_attribute("href")
    
    #loop over prices for discounted price for current li element 
    if len(dcnt_prices) > 0:
        for j in range(0, len(dcnt_prices)):
            price = dcnt_prices[j].get_attribute("innerHTML")                       
            discount_prices_list.append(price)


        #print("item_name length = ", len(item_name))
        for x in range(0, len(item_name)):
            name = item_name[x].get_attribute("href")
            item_name_list.append(name)



'''
check if its getting the same data
'''
print(len(item_name_list))
print(len(discount_prices_list))


'''
prints out a list of tuples that contain the link to the discounted product and its price

Args:
    zip() (method) = takes iterables and combines them in a tuple
    list() (method) = creates a list object
'''
discounted_items = zip(item_name_list,discount_prices_list)
for i in list(discounted_items):
     print(i)



'''
closes the chrome window associated with the code

Args:
    driver.quit() (method) =  quits the whole browser session along with all the associated browser windows
'''
driver.quit()