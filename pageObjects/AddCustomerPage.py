from selenium import webdriver

class AddCustomerPage:

    CustomersMenu_Xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]"
    CustomerMenuitem_Xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]"
    AddNewButton_Xpath="/html/body/div[3]/div[1]/form[1]/div/div/a"
    PlusButton_Xpath="//*[@id='customer-info']/div[1]/div[2]/button/i"
    Email_Id="Email"

    def __init__(self,driver):
        self.driver=driver

    def click_CustomersMenu(self):
        self.driver.find_element_by_xpath(self.CustomersMenu_Xpath).click()

    def click_CustomersMenuItem(self):
        self.driver.find_element_by_Xpath(self.CustomerMenuitem_Xpath).click()

    def click_AddNewwButton(self):
        self.driver.find_element_by_Xpath(self.AddNewButton_Xpath).click()

    def click_PlusButton(self):
        self.driver.find_element_by_Xpath(self.PlusButton_Xpath).click()

    def set_EmailId(self,email):
        self.driver.find_element_by_Xpath(self.Email_Id).send_keys(email)








