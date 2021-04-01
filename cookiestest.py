from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
#chrome
driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  #chrome driver location
driver.get("https://www.amazon.in/")
#get all the cookies
cookies = driver.get_cookies()
print(len(cookies))

print(cookies)

#add new coookie
cookie= {'name':'Mycookie','value':'1234567890'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(len(cookies))

print(cookies)
#cookie delete
driver.delete_cookie('Mycookie')

cookies = driver.get_cookies()
print(len(cookies))

print(cookies)

#delete all ccookies
driver.delete_all_cookies()