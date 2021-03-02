from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
driver.get('file:///C:/Users/Siamen_Silivonchyk/PycharmProjects/PythonAutomationAndTesting/CH02/html_code_02.html')
content = driver.find_element_by_class_name('content')

print('My class element is :')
print(content)

driver.close()
