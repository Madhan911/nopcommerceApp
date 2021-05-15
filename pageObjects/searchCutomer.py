
class searchCustomer:

    text_searchemail_xpath="//input[@id='SearchEmail']"
    text_firstname_xpath="//input[@id='SearchFirstName']"
    text_lastname_xpath="//input[@id='SearchLastName']"
    btn_serch_xpath="//button[@id='search-customers']"

    table_searchresults_xpath="//table[@role='grid']"
    table_xpath="//table[@id='customers-grid']"
    table_rows_xpath="//table[@id='customers-grid']//tbody/tr"
    table_coloumn_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def setEmailsearch(self,email):
        self.driver.find_element_by_xpath(self.text_searchemail_xpath).send_keys(email)

    def setFirstName(self,firstname):
        self.driver.find_element_by_xpath(self.text_firstname_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element_by_xpath(self.text_lastname_xpath).send_keys(lastname)

    def clickonSearch(self):
        self.driver.find_element_by_xpath(self.btn_serch_xpath).click()

    def getNumberOfRows(self):
        return len(self.driver.find_element_by_xpath(self.table_rows_xpath))


    def getNumberOfColumns(self):
        return len(self.driver.find_element_by_xpath(self.table_coloumn_xpath))

    def searchCustomerByEmail(self,email):
        flag = False
        for r in range(1,self.getNumberOfRows()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            emailid=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,firstname):
        flag = False
        for r in range(1,self.getNumberOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            Firstname=table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if Firstname == firstname:
                flag = True
                break
        return flag
