from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driver.get("https://wiki.python.org/moin/FrontPage")
time.sleep(2)
search = driver.find_element_by_id("searchinput")
search.clear()
search.send_keys("Beginner")
search.send_keys(Keys.RETURN)
time.sleep(4)

select = Select(driver.find_element_by_xpath('//div[3]/ul/li[5]/form/div/select'))
select.select_by_visible_text("Raw Text")
time.sleep(4)

driver.close()