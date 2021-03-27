from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
#chrome
driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  #chrome driver location


# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element_by_link_text("Interview Preparation")

# print complete element
print(element)
driver.find_element_by_link_text("Interview Preparation").click()
