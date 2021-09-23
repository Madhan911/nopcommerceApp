# import the webdriver
from selenium import webdriver
# import the Keys class
from selenium.webdriver.common import keys

driver = webdriver.Chrome(executable_path="C:/Users/Nani Madhan/Downloads/chromedriver_win32/chromedriver.exe")
# get method to launch the URL
# driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
#
# driver.maximize_window()
# # to identify the table rows
# rows = driver.find_elements_by_xpath("//tbody/tr")
# cols = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/main/div/article/div/div/form/table/tbody/tr[1]/th")
# # to get the row count len method
# print(len(rows))
# print(len(cols))
# # to close the browser
# driver.quit()

driver.get("https://www.w3.org/WAI/UA/2002/06/thead-test")
driver.maximize_window()
rows = len(driver.find_elements_by_xpath("/html/body/table[3]/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/table[3]/tbody/tr[1]/th"))
print(rows)
print(cols)
print("name"+"         "+"cups"+"    "+"tupeofcoffe"+"   "+"sugar")
for i in range(2, rows+1):
    for j in range(1, cols+1):
        value = driver.find_element_by_xpath("/html/body/table[3]/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
        print(value, end="    ")
    print()

