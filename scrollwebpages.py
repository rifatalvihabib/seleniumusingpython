# import the webdriver
from selenium import webdriver
# import the Keys class
from selenium.webdriver.common import keys
driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")
#
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window() # maximizes window size
#scroll down by pixel
#driver.execute_script('window.scrollBy(0,1000)', "")

#scroll djown until a element is visible

flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[60]/td[1]/img")

#driver.execute_script("arguments[0].scrollIntoView():",flag)

#scroll till end

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
