import pytest
import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customeLogger import logGen
from utilities import XLUtils

class Test_002_DDT_Login:

    baseURL=ReadConfig.getApplicationURL()
    path=".//TestData/DDT.xlsx"
    logger=logGen.loggen()

    def test_DDT_Login(self,setup):
        self.logger.info("*************Test_002_DDT_Login**************")
        self.logger.info("*************test_DDTLogin**************")
        self.row=XLUtils.getRowCount(self.path,"Sheet1")
        lst_status=[]

        for r in range(2,self.row+1):
            self.driver = setup
            self.driver.get(self.baseURL)
            self.username=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)

            self.login=LoginPage(self.driver)
            self.login.set_username(self.username)
            self.login.set_password(self.password)
            self.login.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info("*************Passed***********")
                    #self.login.clicklogout()
                    lst_status.append("Pass")
                elif self.exp=='Fail':
                    self.logger.info("***************Failed***********")
                    #self.login.clicklogout()
                    lst_status.append("Fail")
                self.login.clicklogout()
            elif act_title != exp_title:
                if self.exp=='Pass':
                    self.logger.info("*************Failed***********")
                    #self.login.clicklogout()
                    lst_status.append("Fail")
                elif self.exp=='Fail':
                    self.logger.info("***************Passed***********")
                    #self.login.clicklogout()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("***************Login_DDT_TC_Passed*************")
            assert True
            self.driver.close()
        else:
            self.logger.info("***************Login_DDT_TC_failed*************")
            self.driver.close()
            assert False

        self.logger.info("***********End of DDT Login*********")
        self.logger.info("***********Completed Test_002_DDT_Login***************")









