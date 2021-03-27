from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  #chrome driver location
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407") #get the url

# Selecting radio button
# Select male
driver.find_element_by_xpath(
    '//*[@id="q26"]/table/tbody/tr[2]/td/label').click()

#working with checkboxes

# Selecting check box
# Select sunday
driver.find_element_by_xpath(
    '//*[@id="q15"]/table/tbody/tr[1]/td/label').click()


# Select monday
driver.find_element_by_xpath(
    '//*[@id="q15"]/table/tbody/tr[2]/td/label').click()
ele= driver.find_element_by_xpath(
    "/html[1]/body[1]/form[1]/div[2]/div[17]/table[1]/tbody[1]/tr[2]/td[1]/input[1]").is_selected()
print(ele)