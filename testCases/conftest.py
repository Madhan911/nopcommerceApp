from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def setup(browser):
    if browser == 'Chrome':
        driver = webdriver.Chrome(executable_path="C:/Users/Nani Madhan/Downloads/chromedriver_win32/chromedriver.exe")
        print("launching Chrome")
    elif browser == 'Firefox':
        driver = webdriver.Firefox(executable_path="C:/Users/Hp/Desktop/New nani/geckodriver.exe")
        print("launching firefox")
    else:
        driver = webdriver.Ie(executable_path="C:/Users/Hp/DesktopNew nani/IEDriverServer")
        print("launching ie")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="function")
def browser(request):
    return request.config.getoption("--browser")


'''
def pytest_configure(config):
    config._metadata['project name'] = 'nop commerce'
    config._metadata['module name'] = 'customers'
    config._metadata['Tester'] = 'madhan'
    
'''


