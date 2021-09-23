import pytest
from selenium import webdriver
import time


class TestWindow:

    def testWindow(self):
        driver = webdriver.Chrome(executable_path="C:/Users/Nani Madhan/Downloads/chromedriver_win32/chromedriver.exe")
        driver.get("https://mtouch.facebook.com/login/")
        driver.maximize_window()
        parent_window = driver.current_window_handle
        time.sleep(3)
        driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
        driver.maximize_window()
        child_window = driver.window_handles
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("nani")
        time.sleep(3)
        # driver.switch_to_window(parent_window)
        for child in child_window:
            print(child)
