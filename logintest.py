from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
#chrome
driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  #chrome driver location

driver.get("http://prm.dnet.org.bd/login") #get the url

print(driver.title) #title of the page
user_ele = driver.find_element_by_name("email")
print(user_ele.is_displayed())  #returns true or false based of element status
print(user_ele.is_enabled())       #returns true or false based of element status
pwd_ele = driver.find_element_by_name("password")

print(pwd_ele.is_displayed())  #returns true or false based of element status
print(pwd_ele.is_enabled())       #returns true or false based of element status


user_ele.send_keys("rifat.alvi@dnet.org.bd")
pwd_ele .send_keys("mdk6family")
driver.find_element_by_xpath("//*[@id='app']/main/div/div/div/div/div[2]/form/div[4]/button").click()
#driver.find_element_by_css_selector("input[value=roundtrip]")
#is_selected is to check radio buttons
# name attribute same.so we are choosing the value

print(driver.title) #title of the page