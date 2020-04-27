from selenium.webdriver.common.by import By

from TestProjectXero.Demo.Locators import Locators
class Bank_Accounts(object):


    def __init__( self, driver ):
            self.driver = driver

    def Org(self):
        self.driver.find_element(By.CLASS_NAME, Locators.Locators.Current_Org).click()

    def Find_your_bank(self, bank_name):
        self.driver.find_element(By.XPATH, Locators.Locators.Bank_Name).send_keys(bank_name)

        # test.send_keys(Keys.TAB)

    def Result( self ):
        self.driver.find_element(By.XPATH, Locators.Locators.Results)


    def Account_name(self, acc_name):
       self.driver.find_element(By.XPATH, Locators.Locators.AccountName).send_keys(acc_name)

    def Account_Type(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.Locators.Account_type_dropdown).click()
        self.driver.find_element(By.CSS_SELECTOR,Locators.Locators.Account_type_selection).click()


    def Account_number(self, acc_number):
        self.driver.find_element(By.XPATH, Locators.Locators.AccountNumber).send_keys(acc_number)

    def Continue(self):
        self.driver.find_element(By.CSS_SELECTOR , Locators.Locators.Continue_button).click()

