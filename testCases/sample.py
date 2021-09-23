import pytest
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/Nani Madhan/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://mtouch.facebook.com/login/")
driver.maximize_window()
time.sleep(3)
driver.close()
