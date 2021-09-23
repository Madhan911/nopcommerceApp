from tkinter import Image

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C://Users//Nani Madhan//Downloads//chromedriver_win32//chromedriver.exe")
driver.get("https://www.testandquiz.com/selenium/testing.html")
driver.maximize_window()
driver.implicitly_wait(3)

select = Select(driver.find_element_by_xpath('/html/body/div/div[9]/div/p/select'))

# select by visible text
# select.select_by_visible_text('Manual Testing')

# select by value
#select.select_by_value('3')
select.select_by_index('2')

driver.save_screenshot("image.png")


image = Image.open("image.png")
image.show()
