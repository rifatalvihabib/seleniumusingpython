import XLUtils
from  selenium import  webdriver


driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  #chrome driver location

driver.get("http://prm.dnet.org.bd/login") #get the url

driver.maximize_window()
path="D:\Seleniumbasics\dd.xlsx"
rows=XLUtils.getRowCount(path,'Sheet1')

for r in range(2, rows+1):
    username = XLUtils.readData(path,"Sheet1",r,1)
    password = XLUtils.readData(path,"Sheet1",r,2)

    user_ele = driver.find_element_by_name("email")
    user_ele.send_keys(username)
    pwd_ele = driver.find_element_by_name("password")
    pwd_ele.send_keys(password)
    driver.find_element_by_xpath("//*[@id='app']/main/div/div/div/div/div[2]/form/div[4]/button").click()

    if driver.current_url == "http://prm.dnet.org.bd/home":
        print("TEst passed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test passed")
        driver.close()


    else :
        print("test failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test failed")
        driver.refresh()


driver.get("http://prm.dnet.org.bd/login")  # get the url
    #Project Resource Management




