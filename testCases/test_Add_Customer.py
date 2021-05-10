from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage
from utilities.readProperties import ReadConfig
import random
import string

class Test_003_add_Customer:

    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getApplicationusername()
    password=ReadConfig.getApplicationpassword()

    def test_add_Customer(self,setup):

        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.clickLogin()

        self.addcust=AddCustomerPage(self.driver)
        self.addcust.click_CustomersMenu()
        self.addcust.click_CustomersMenuItem()
        self.addcust.click_AddNewwButton()
        self.addcust.click_PlusButton()

        self.email=random_generator()+"@gmail.com"
        self.addcust.set_EmailId(self.email)

        act_title = self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.logger.info("*************test_homePgeTitle Passed**************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePgeTitle.png")
            self.driver.close()
            self.logger.error("*************test_homePgeTitle Failed**************")
            assert False

def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))



