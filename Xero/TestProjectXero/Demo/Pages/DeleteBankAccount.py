from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from TestProjectXero.Demo.Locators import Locators


class Delete_Bank_Accounts(object):

    def __init__( self, driver ):
            self.driver = driver

    def Navigate_to_Charts_of_BankAccounts(self):
        self.driver.find_element(By.XPATH, Locators.Locators.Accounting_link).click()
        self.driver.find_element(By.LINK_TEXT, Locators.Locators.Chart_Of_bank_Acc).click()

    def Search_bank_account(self, bank_account_name):

        self.driver.find_element(By.XPATH, Locators.Locators.SearchBox).send_keys(bank_account_name)
        self.driver.find_element(By.ID, 'SearchTermsText').send_keys(Keys.ENTER)

        time.sleep(10)

    def Delete_bank_account(self):
        self.driver.find_element(By.XPATH, Locators.Locators.CheckboxToSelect).click()
        time.sleep(10)

        self.driver.find_element_by_link_text('Delete').is_enabled
        self.driver.find_element_by_link_text('Delete').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Locators.Locators.ConfirmDelete).click()




