from selenium import webdriver
import time

driver= webdriver.Chrome('C:/chromedriver/chromedriver.exe')
driver.get('http://seleniumhq.org')
time.sleep(2)

driver.close()
