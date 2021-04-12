from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
#chrome
driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  #chrome driver location

driver.get("http://testautomationpractice.blogspot.com/") #get the url

button = driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button")

button.click()

#Switch the control to the Alert window
obj = driver.switch_to.alert

#Retrieve the message on the Alert window
msg=obj.text
print ("Alert shows following message: "+ msg )

time.sleep(2)

#use the accept() method to accept the alert
obj.accept()

print(" Clicked on the OK Button in the Alert Window")

driver.close