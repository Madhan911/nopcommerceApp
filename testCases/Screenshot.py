from time import sleep

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://Users//Nani Madhan//Downloads//chromedriver_win32//chromedriver.exe")
driver.get("https://www.lambdatest.com/blog/python-selenium-screenshots/")
sleep(1)
#driver.save_screenshot("C://Users//Nani Madhan//OneDrive//Desktop//iam.png")
driver.save_screenshot("C://Users//Nani Madhan//PycharmProjects//nopcommerceApp//BasicPrograms//iam.png")
