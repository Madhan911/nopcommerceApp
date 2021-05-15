import time


import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utitlities.readProperties import readConfig
from utitlities.customLogger import LogGen
from pageObjects.addCutomer import AddCustomer
from pageObjects.searchCutomer import searchCustomer
from selenium.webdriver.common.keys import Keys
import string
import random



class Test_004_Login:

    baseURL = readConfig.getApllicationURL()
    username = readConfig.getUseremail()
    password = readConfig.getPassword()
    logger = LogGen.loggingDmo()

    @pytest.mark.sanity
    def test_searchCustomers(self,setup):

        self.logger.info("****************Test_001_Login*************  ")
        self.logger.info("**************** Started *************  ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.lp = LoginPage(self.driver)
        self.driver.implicitly_wait(5)
        self.lp.setUserName(self.username)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        self.logger.info("*************** Login sucessful *************  ")

        self.addCust = AddCustomer(self.driver)
        self.driver.implicitly_wait(5)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerMenuButton()
        self.driver.implicitly_wait(5)


        self.searchcust = searchCustomer(self.driver)
        self.driver.implicitly_wait(5)
        self.searchcust.setEmailsearch("victoria_victoria@nopCommerce.com")
        self.searchcust.clickonSearch()
        time.sleep(5)
        status=self.searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.driver.close()





