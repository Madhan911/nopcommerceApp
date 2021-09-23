# import webdriver
from selenium import webdriver

import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="C:/Users/Nani Madhan/Downloads/chromedriver_win32/chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
#to refresh the browser
driver.refresh()
#click on submit button
#driver.find_element_by_xpath("//button[@name='submit']").click()
driver.execute_script("alert('this is madhan');")

time.sleep(5)


# alert object creation and switching focus to alert
a = driver.switch_to.alert
# accept the alert
a.accept()
driver.close()


