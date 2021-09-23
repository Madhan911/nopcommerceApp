from selenium import webdriver

DEMO_PAGE = '''data:text/html,
    <p>Demo page for how to get text from hidden elements using Selenium WebDriver.</p>
    <div id='demo-div'>Demo div <p style='display:none'>with a hidden paragraph inside.</p><hr /><br /></div>'''

driver = webdriver.PhantomJS()
driver.get(DEMO_PAGE)

demo_div = driver.find_element_by_id("demo-div")

print(demo_div.get_attribute('innerHTML'))
print(driver.execute_script("return arguments[0].innerHTML", demo_div))

print(demo_div.get_attribute('textContent'))
print(driver.execute_script("return arguments[0].textContent", demo_div))

driver.quit