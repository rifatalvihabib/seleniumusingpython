from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
#chrome
driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  #chrome driver location

driver.get("http://demo.automationtesting.in/Windows.html") #get the url
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

print(driver.current_window_handle) #parent handle

handles = driver.window_handles #every window handle
for handle in handles:
    driver.switch_to.window(handle) # currently open window handle print
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close() #closes parent window
driver.quit() #will close all browser windows