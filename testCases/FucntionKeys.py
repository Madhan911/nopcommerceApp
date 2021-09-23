import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C://Users//Nani Madhan//Downloads//chromedriver_win32//chromedriver.exe")
driver.get("https://www.testandquiz.com/selenium/testing.html")
driver.maximize_window()
driver.implicitly_wait(3)
# driver.find_element_by_id("fname").click()
# function keys
A = ActionChains(driver)
# A.send_keys(Keys.TAB).perform()
# A.click(driver.find_element_by_xpath("/html/body/div/div[6]/div/p/button")).perform()


# copy paste
driver.find_element_by_id("fname").send_keys("madhan")
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.Id, "fname")))

driver.implicitly_wait(2)

A.key_down(Keys.CONTROL).send_keys("a")
driver.implicitly_wait(2)
# A.key_down(Keys.CONTROL).send_keys("x")
