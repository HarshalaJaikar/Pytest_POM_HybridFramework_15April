import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customeLogger import logGen

class Test_001_Login:

    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getApplicationusername()
    password=ReadConfig.getApplicationpassword()

    logger=logGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_homePgeTitle(self,setup):

        self.logger.info("*************Test_001_Login**************")
        self.logger.info("*************test_homePgeTitle**************")
        self.driver= setup
        self.driver.get("https://admin-demo.nopcommerce.com/admin/")
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.logger.info("*************test_homePgeTitle Passed**************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePgeTitle.png")
            self.driver.close()
            self.logger.error("*************test_homePgeTitle Failed**************")
            assert False


    def test_Login(self,setup):
        self.logger.info("*************test_Login**************")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.login=LoginPage(self.driver)
        self.login.set_username(self.username)
        self.login.set_password(self.password)
        self.login.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*************test_Login Passed**************")
            self.driver.close()
        else:
            assert False
            self.logger.error("*************test_Login Failed**************")
            self.driver.close()


