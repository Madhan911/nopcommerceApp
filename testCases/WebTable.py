import pytest
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/Nani Madhan/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://chercher.tech/practice/table")

cols = len(driver.find_elements_by_xpath("/html/body/div/div/div/div/div[1]/table/tbody/tr"))

rows = len(driver.find_elements_by_xpath("/html/body/div/div/div/div/div[1]/table/tbody/tr[1]/th"))

for r in range(2, rows+1):
    for c in range(1, cols+1):
        print(c.text)
    print(r.text)

