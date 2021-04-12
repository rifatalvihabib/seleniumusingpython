from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  #chrome driver location

driver.get("https://www.selenium.dev/") #get the url

driver.maximize_window() #maximize the window
try:
    element = WebDriverWait(driver, 10).until(

    EC.presence_of_element_located((By.XPATH, '//*[@id="aboutArrow"]')) # wait for max 10 until about down arrow found
    )
finally:
    # click the element
    element.click()

driver.find_element_by_xpath('//*[@id="aboutSubnav"]/div[1]/a').click() #click about

tocheck = "Selenium is a suite of tools for automating web browsers." # store in a variable what to check


try:
    element1 = WebDriverWait(driver, 10).until(

    EC.presence_of_element_located((By.XPATH, '/html/body/section/div/p')) # wait for max 10 until text element found
    )
finally:
    assert element1.text == tocheck


driver.back()


