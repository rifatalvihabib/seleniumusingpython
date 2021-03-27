# import webdriver
from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  #chrome driver location

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get  element
element = driver.find_element_by_link_text("Courses")

# create action chain object
action = ActionChains(driver)

# perform the operation
action.move_to_element(element).click().perform()