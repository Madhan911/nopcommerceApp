import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utitlities.readProperties import readConfig
from utitlities.customLogger import LogGen
from pageObjects.addCutomer import AddCustomer
import string
import random



class Test_003_Login:

    baseURL = readConfig.getApllicationURL()
    username = readConfig.getUseremail()
    password = readConfig.getPassword()
    logger = LogGen.loggingDmo()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):

        self.logger.info("****************Test_001_Login*************  ")
        self.logger.info("**************** Started *************  ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        self.logger.info("*************** Login sucessful *************  ")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerMenuButton()
        self.addCust.addNewButton()

        def id_generator(size=8, chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for x in range(size))


        self.email = id_generator() + "@gmail.com"
        time.sleep(3)
        self.addCust.setEmial(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("NANI")
        self.addCust.setLastName("NANI")
        self.addCust.setGender("/Male")
        time.sleep(3)
        self.addCust.doBirth("1/8/2020")
        self.addCust.companyName("LEGATO")
        self.addCust.setCustomerRoles("Vendors")
        self.addCust.setMangerOfVendor("Vendor 1")
        time.sleep(2)
        #self.addCust.newsLetter("Test store 2")
        self.addCust.adminComment("i am a good learner in python")
        self.logger.info("Member info entered sucessfully *************  ")
        self.addCust.clickOnSave()


        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True

        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\" + "addCustomer.png")
            assert True == False

        self.logger.info("**********The new customer has been added successfully*************  ")
        self.driver.close()
        #commit changes






