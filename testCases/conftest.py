from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path="C:/Users/comp/PycharmProjects/Pytest_POM_HybridFramework_15April/Driver/chromedriver.exe")
    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path="C:/Users/comp/PycharmProjects/Pytest_POM_HybridFramework_15April/Driver/geckodriver.exe")
    else:
        driver=webdriver.Chrome(executable_path="C:/Users/comp/PycharmProjects/Pytest_POM_HybridFramework_15April/Driver/chromedriver.exe")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project_Name']='Hybrid Framework'
    config._metadata['Module_Name']='Customers'
    config._metadata['Tester']='Harshala'



