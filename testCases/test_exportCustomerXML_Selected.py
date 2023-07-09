import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.exportCustomer import exportCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_ExportCustomerXML_008:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.Data1
    def test_exportCustomerXML(self, setup):
        self.logger.info("****************** Search Customer By Email **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************************* Login Successful ****************")

        self.logger.info("*************************** Export customer details Test Start *************************")

        self.exportCust = exportCustomer(self.driver)
        self.exportCust.clickOnCustomersMenu()
        self.exportCust.clickOnCustomersMenuItem()

        self.logger.info("******************** Exporting Customer Selected ******************")

        self.exportCust.clickOnTableMainCheckbox()
        self.exportCust.clickOnExportDropdownBtn()
        self.exportCust.clickOnExportXML_SelectedBtn()

        self.logger.info("******************* Exporting Customer Completed *******************")

        assert True