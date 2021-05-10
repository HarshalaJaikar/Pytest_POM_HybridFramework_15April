from selenium import webdriver

class SearchCustomerPage:

    Customers_Menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]"
    Customer_SubMenu_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]"
    Email_inputbox_Id = "SearchEmail"
    Search_button_xpath="//*[@id='search-customers']"

    tbleSearchResults_xpath="//table[@role='grid']"
    table_xpath="//*[@id='customers-grid']"
    table_row_xpath="//*[@id='customers-grid']/tbody/tr"
    table_col_xpath="//*[@id='customers-grid']/tbody/tr/td"


    def __init__(self,driver):
        self.driver=driver

    def click_CustomersMenu(self):
        self.driver.find_element_by_xpath(self.Customers_Menu_xpath).click()

    def click_CustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.Customer_SubMenu_Xpath).click()

    def set_mail(self,email):
        self.driver.find_element_by_id(self.Email_inputbox_Id).clear()
        self.driver.find_element_by_id(self.Email_inputbox_Id).send_keys(email)

    def click_search(self):
        self.driver.find_element_by_xpath(self.Search_button_xpath).click()

    def get_no_of_rows(self):
        return len(self.driver.find_elements_by_xpath(self.table_row_xpath))

    def get_no_of_columns(self):
        return len(self.driver.find_elements_by_xpath(self.table_col_xpath))

    def search_Customer_by_Email(self,email):
       # flag = False
        for r in range(1,self.get_no_of_rows()+1):
            emailid = self.driver.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text

            print(emailid)
            if email==emailid:
                return True
            else:
                return False




