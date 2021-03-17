from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
driver.get('http://www.seleniumhq.org')

element_id_q = driver.find_element_by_id('q')
print(element_id_q)
element_name_q = driver.find_element_by_name('q')
print(element_name_q)
element_class = driver.find_element_by_class_name('selenium-backer')
print(element_class)
element_xpath = driver.find_element_by_xpath('//html/body/section[1]/h1[2]')
print(element_xpath)

driver.close()