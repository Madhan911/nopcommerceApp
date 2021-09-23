from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome(executable_path="C://Users//Nani Madhan//Downloads//chromedriver_win32//chromedriver.exe")
url = "https://www.google.com/"
driver.get(url)
driver.save_screenshot("ss.png")
screenshot = Image.open("ss.png")
screenshot.show()