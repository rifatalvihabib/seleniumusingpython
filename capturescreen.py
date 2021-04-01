from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
#chrome
driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  #chrome driver location
driver.get("https://www.amazon.in/")
#driver.save_screenshot("D:\selenium with python\damzn.jpg") #any image type
driver.get_screenshot_as_file("D:\selenium with python\damzn.png") #png only