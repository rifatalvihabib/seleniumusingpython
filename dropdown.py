# Import required module
import time
from selenium import webdriver

# Import Select class
from selenium.webdriver.support.ui import Select
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  #chrome driver location
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407") #get the url


# Find id of option
x = driver.find_element_by_id('RESULT_RadioButton-9')
drop = Select(x)

# Select by value
drop.select_by_value('Radio-0')
time.sleep(4)
# Select by index
drop.select_by_index(2)
time.sleep(4)
driver.close()