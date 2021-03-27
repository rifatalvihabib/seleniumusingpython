# import the webdriver
from selenium import webdriver
# import the Keys class
from selenium.webdriver.common import keys
driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")
# get method to launch the URL
u="https://www.softwaretestingmaterial.com/sample-webpage-to-automate/"
driver. get (u)
# to identify the table rows
r = driver.find_elements_by_xpath ("//tbody/tr")
# to identify table columns
c = driver.find_elements_by_xpath ("//tbody/tr[1]/th")
# to get row count with len method
rc = len (r)

# to get column count with len method
cc = len (c)
# to traverse through the table rows excluding headers
for i in range (2, rc + 1) :

     #to traverse through the table column
     for j in range (2, cc + 1) :

#to get all the cell data with text method
        d = driver.find_element_by_xpath ("//tr["+str(i)+"]/td["+str(j)+"]").text
        print (d)
#to close the browser
driver.close ()