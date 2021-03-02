from selenium import webdriver
driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
driver.get('file:///C:/Users/Siamen_Silivonchyk/PycharmProjects/PythonAutomationAndTesting/CH02/html_code_02.html')
username = driver.find_element_by_name('username')
print('My input element is:')
print(username)
driver.close()