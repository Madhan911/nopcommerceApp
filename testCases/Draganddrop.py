from tkinter import Image

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from PIL import Image

driver = webdriver.Chrome(executable_path="C://Users//Nani Madhan//Downloads//chromedriver_win32//chromedriver.exe")
driver.get("https://css-tricks.com/drag-and-drop-file-uploading/")
driver.maximize_window()
driver.implicitly_wait(3)

sorce_element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[2]/div[1]/a/img")
target_element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/main/article/div[2]/div/figure/img")

drag = ActionChains(driver)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# drag.drag_and_drop(sorce_element, target_element).perform()
drag.drag_and_drop_by_offset(sorce_element, 432, 239).perform()

#drag.click_and_hold(sorce_element).move_to_element(target_element).perform()
driver.save_screenshot("C://Users//Nani Madhan//PycharmProjects//nopcommerceApp//New//nani.png")
# screenshot = Image.open("nani.png")
# screenshot.show()
