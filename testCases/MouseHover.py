from tkinter import Image

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from PIL import Image

driver = webdriver.Chrome(executable_path="C://Users//Nani Madhan//Downloads//chromedriver_win32//chromedriver.exe")

driver.get("https://www.orangehrm.com/contact-sales/")
submit = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/form/fieldset/div[2]/div")
actions = ActionChains(driver)
actions.move_to_element(submit).click().perform()
