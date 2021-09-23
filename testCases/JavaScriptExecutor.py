from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/Nani Madhan/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://classic.crmpro.com/index.html")
time.sleep(5)
for_pss = driver.find_element_by_xpath("//a[contains(text(),'Forgot Password?')]")
driver.execute_script("arguments[0].scrollIntoView(true);", for_pss)
