from selenium.webdriver.common.by import By

from TestProjectXero.Demo.Locators import Locators


class Homepage(object):

    def __init__( self, driver ):
        self.driver = driver

    def link_to_Accounting( self ):
        self.driver.find_element(By.XPATH, Locators.Locators.Accounting_link).click()

    def link_to_Bank_Accounts( self ):
        self.driver.find_element_by_link_text(Locators.Locators.BankAccount_link).click()


    def Add_bank_Account_link( self ):
        self.driver.find_element(By.XPATH, Locators.Locators.Add_bank_account).click()



