import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    textbox_username_id ="Email"
    textbox_password_id ="Password"
    button_login_xpath ="//button[contains(text(),'Log in')]"
    link_customermenupath_xpath ="//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]"
    link_customermenupathbutton_xpath ="//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]"
    btn_addbutton_xpath ="//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    textbox_email_xpath ="//input[@id='Email']"
    textbox_password_xpath ="//input[@id='Password']"
    textbox_firstname_xpath ="//input[@id='FirstName']"
    textbox_lastname_xpath ="//input[@id='LastName']"

    rd_male_xpath ="//input[@id='Gender_Male']"
    rd_female_xpath ="//input[@id='Gender_Female']"

    textbox_dob_xpath ="//input[@id='DateOfBirth']"
    textbox_compname_xpath ="//input[@id='Company']"
    rd_taxe_xmpt_xpath ="//input[@id='IsTaxExempt']"

    textbox_newsletter_xpath ="//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]"
    listitem_storename_xpath ="//li[contains(text(),'Your store name')]"
    listitem_storetwo_xpath ="//li[contains(text(),'Test store 2')]"

    textbox_customerroles_xpath ="//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]"
    listitem_customerroles_admin_xpath ="//li[contains(text(),'Administrators')]"
    listitem_customerroles_forummoderaters_xpath ="//li[contains(text(),'Forum Moderators')]"
    listitem_customerroles_guests_xpath ="//li[contains(text(),'Guests')]"
    listtiem_cutomeerriles_registered_xpath ="//li[contains(text(),'Registered')]"
    listtiem_cutomeerriles_vendors_xpath =" //li[contains(text(),'Vendors')]"

    drpdown_vendor_xpath ="//select[@id='VendorId']"
    rd_active_xpath =" //input[@id='Active']"
    textbox_admincontent_xpath ="//textarea[@id='AdminComment']"
    btn_save_xpath ="//body/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]"





    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.link_customermenupath_xpath).click()

    def clickOnCustomerMenuButton(self):
        self.driver.find_element_by_xpath(self.link_customermenupathbutton_xpath).click()

    def addNewButton(self):
        self.driver.find_element_by_xpath(self.btn_addbutton_xpath).click()

    def setEmial(self, email):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element_by_xpath(self.textbox_firstname_xpath).send_keys(firstname)

    def setLastName(self, Lastname):
        self.driver.find_element_by_xpath(self.textbox_lastname_xpath).send_keys(Lastname)

    def doBirth(self, dob):
        self.driver.find_element_by_xpath(self.textbox_dob_xpath).send_keys(dob)

    def companyName(self, companyname):
        self.driver.find_element_by_xpath(self.textbox_compname_xpath).send_keys(companyname)

    def adminComment(self, admincomment):
        self.driver.find_element_by_xpath(self.textbox_admincontent_xpath).send_keys(admincomment)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()


    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_xpath(self.rd_male_xpath).click()
        elif gender == 'female':
            self.driver.find_element_by_xpath(self.rd_female_xpath).click()

        else:
            self.driver.find_element_by_xpath(self.rd_male_xpath).click()

    def setMangerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpdown_vendor_xpath))
        drp.select_by_visible_text(value)

    '''def newsLetter(self, news):
        news = Select(self.driver.find_element_by_xpath(self.textbox_newsletter_xpath))
        news.select_by_visible_text(news)'''
    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.textbox_customerroles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.listtiem_cutomeerriles_registered_xpath)
        elif role == "Adminisrtators":
            self.listitem = self.driver.find_element_by_xpath(self.listitem_customerroles_admin_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.listtiem_cutomeerriles_registered_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.listtiem_cutomeerriles_vendors_xpath)
        elif role == "Guests":
            #here user can regesterd or guest only
            time.sleep(3)
            self.driver.find_element_by_xpath("//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.listitem_customerroles_guests_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.listitem_customerroles_guests_xpath)
            time.sleep(3)
            #self.listitem.click()
            self.driver.execute_script("arguments[0].click();", self.listitem)































    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()



