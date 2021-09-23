import requests
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(executable_path="C:/Users/Nani Madhan/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://google.co.in/')
links = driver.find_elements_by_css_selector("a")
for link in links:
    r = requests.head(link.get_attribute('href'))
    print(link.get_attribute('href'), r.status_code)

'''webdriver.get(PAGEURL)

links = webdriver.find_elements_by_css_selector("a")

for link in links:

  if (requests.head(link.get_attribute('href')).status_code == 200):
  print("Valid link")
  else:
  print("Broken link")'''