from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")
driver.implicitly_wait(0.5)
driver.maximize_window()

driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
#to identify element
s = driver.find_element_by_xpath("//input[@type='file']")
#file path specified with send_keys forward slash
s.send_keys("D://Seleniumbasics/DSC06100.JPG")