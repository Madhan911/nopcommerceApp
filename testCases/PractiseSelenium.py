from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium import webdriver

from selenium.webdriver import ActionChains


driver = webdriver.Chrome(executable_path="C:/Users/Nani Madhan/Downloads/chromedriver_win32/chromedriver.exe")
# this is explict wait
wait = WebDriverWait(driver, 10)
element = wait.Until(EC.title_is((By.ID, 'someid')))

# send text without using the send_keys method in python
driver.execute_script("document.getElementById('user').value='tester'")

# scroll down till xpath is mentioned
flag = driver.find_element_by_xpath("xpath")
driver.execute_script("arguments[0].scrollIntoView();", flag)

# scroll down till page is down
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")




# import Action chains

# create webdriver object
driver = webdriver.Firefox()
# create action chain object
action = ActionChains(driver)
# right click and double click
# import actionschains and create chains object
action.double_click().perform()
action.context_click().perform()

#this is for click method for javascript method
driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//button[@name='username']"))

#this is second way
userName = driver.find_element_by_xpath("//button[@name='username']")
driver.execute_script("arguments[0].click();", userName)