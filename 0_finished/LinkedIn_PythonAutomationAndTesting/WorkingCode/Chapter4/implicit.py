from selenium import webdriver

driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driver.implicitly_wait(10)

driver.get("http://www.python.org")
myDynamicElement = driver.find_element_by_id("start-shell")

driver.close()