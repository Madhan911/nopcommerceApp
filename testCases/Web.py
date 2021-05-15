from selenium import webdriver
import pytest
import time

class TestWebApplication():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(executable_path="C:/Users/Hp/Desktop/New nani/chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePage(self,setup):
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        time.sleep(2)
        assert self.driver.title == "Your store. Login"

    @pytest.mark.regression
    def test_loginPage(self,setup):
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        self.driver.find_element_by_id("Email").clear()
        self.driver.find_element_by_id("Email").send_keys("admin@yourstore.com")
        self.driver.find_element_by_id("Password").clear()
        self.driver.find_element_by_id("Password").send_keys("admin")
        self.driver.find_element_by_xpath("//button[contains(text(),'Log in')]").click()
        time.sleep(2)
        assert self.driver.title == "Dashboard / nopCommerce administration"
        self.driver.find_element_by_link_text("Logout").click()
        assert self.driver.title == "Dashboard / nopCommerce administration"







