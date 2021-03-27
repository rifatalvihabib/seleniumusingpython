
# importing the modules
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# using chrome driver
driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  #chrome driver location

# web page url
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

# switch to 1st frame
driver.switch_to.frame("packageListFrame")

# click on 1st frame
driver.find_element_by_link_text("org.openqa.selenium.opera").click()

# back to default web page frame
driver.switch_to.default_content()

# switch to 2nd frame
driver.switch_to.frame("packageFrame")

# click on  2nd frame
driver.find_element_by_link_text("OperaOptions").click()

# back to default web page frame
driver.switch_to.default_content()

# switch to 3rd frame
driver.switch_to.frame("classFrame")

# click on  2nd frame
driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[1]/ul/li[6]').click()
time.sleep(4)