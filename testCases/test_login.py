import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utitlities.readProperties import readConfig
from utitlities.customLogger import LogGen



class Test_001_Login:
    baseURL = readConfig.getApllicationURL()
    username = readConfig.getUseremail()
    password = readConfig.getPassword()

    logger=LogGen.loggingDmo()


    @pytest.mark.regression
    def test_homepageTitel(self,setup):

        self.logger.info("****************Test_001_Login*************  ")
        self.logger.info("**************** Verifiing home page title *************  ")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****************Homepage title test is passed *************  ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitel.png")
            self.driver.close()
            self.logger.error("****************Homepage title test is failed *************  ")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("**************** Verifiing login test *************  ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("****************Login test is passed *************  ")
        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("****************Login test is failed *************  ")
            assert False
