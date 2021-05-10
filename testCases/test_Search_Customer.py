import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customeLogger import logGen
import time

class Test_004_searchCust:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationusername()
    password = ReadConfig.getApplicationpassword()

    logger = logGen.loggen()

    @pytest.mark.sanity
    #@pytest.mark.regression
    def test_searchCustomer(self,setup):

        self.logger.info("*************Test_001_Login***********")
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/admin/")

        self.login = LoginPage(self.driver)
        self.login.set_username(self.username)
        self.login.set_password(self.password)
        self.login.clickLogin()
        time.sleep(8)

        self.srchcust = SearchCustomerPage(self.driver)
        self.srchcust.click_CustomersMenu()
        time.sleep(3)
        self.srchcust.click_CustomersMenuItem()
        time.sleep(3)
        self.srchcust.set_mail("victoria_victoria@nopCommerce.com")
        self.srchcust.click_search()
        time.sleep(5)
        print(self.srchcust.get_no_of_rows())
        status=self.srchcust.search_Customer_by_Email("victoria_victoria@nopCommerce.com")
        time.sleep(5)
        assert status==True
