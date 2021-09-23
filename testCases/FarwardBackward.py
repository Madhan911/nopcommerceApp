import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create webdriver object
driver = webdriver.Chrome(executable_path="C:/Users/Nani Madhan/Downloads/chromedriver_win32/chromedriver.exe")

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

driver.maximize_window()

element = WebDriverWait(driver, 10).until(EC.s((By.ID, "myDynamicElement")))




driver.implicitly_wait(5)

# get geeksforgeeks.org
try:
    driver.get("https://www.practice.geeksforgeeks.org/")
except WebDriverException:
    print("page down")

# one step backward in browser history
driver.back()

# one step backward in browser history
driver.forward()

driver.refresh()


driver.window_


