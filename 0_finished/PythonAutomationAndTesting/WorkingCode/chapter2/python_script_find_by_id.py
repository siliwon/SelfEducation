from selenium import webdriver
driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
driver.get('file:///C:/Users/Siamen_Silivonchyk/PycharmProjects/PythonAutomationAndTesting/CH02/html_code_02.html')
login_form = driver.find_element_by_id('loginForm')
print('My login form element is:')
print(login_form)
driver.close()