import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from TestProjectXero.Demo.Pages import BankAccountPage
from TestProjectXero.Demo.Pages import Homepage
from TestProjectXero.Demo.Locators import Locators
from TestProjectXero.Demo.Pages import Login
from TestProjectXero.Demo.Pages import DeleteBankAccount
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


def test_Add_Dup_Bank_Account(self):
    Homepage.Homepage.link_to_Accounting(self)
    Homepage.Homepage.link_to_Bank_Accounts(self)
    Homepage.Homepage.Add_bank_Account_link(self)
    wait = WebDriverWait(self.driver, 10)
    time.sleep(5)

    # Add bank account
    BankAccountPage.Bank_Accounts.Account(self, 'ANZ (NZ)')

    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ba-banklist--title")))
    self.driver.find_element(By.XPATH, Locators.Locators.Search_For_ANZ).send_keys(Keys.TAB)

    self.driver.find_element(By.ID, Locators.Locators.Select_ANZ).click()

    element = WebDriverWait(self.driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.Locators.Acct_Name_Field))
    )
    element.click()

    # Add Account Name
    words = ['PRIYA', 'NEWZEALAND', 'INDIA', 'AFRICA', 'ISLAND']
    dup_bank_name = random.choice(words)

    BankAccountPage.Bank_Accounts.Account_name(self, dup_bank_name)
    BankAccountPage.Bank_Accounts.Account_Type(self)

    self.driver.find_element(By.XPATH, '//input[@componentid="accountnumber-1068"]').send_keys('11111')
    BankAccountPage.Bank_Accounts.Continue(self)
    time.sleep(5)

    Homepage.Homepage.Add_bank_Account_link(self)
    time.sleep(5)
    # Add bank account
    BankAccountPage.Bank_Accounts.Account(self, 'ANZ (NZ)')
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ba-banklist--title")))
    self.driver.find_element(By.XPATH, Locators.Locators.Search_For_ANZ).send_keys(Keys.TAB)

    self.driver.find_element(By.ID, Locators.Locators.Select_ANZ).click()

    element = WebDriverWait(self.driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.Locators.Acct_Name_Field))
    )
    element.click()
    # BankAccountPage.Bank_Accounts.Account(self, 'ANZ (NZ)')
    # time.sleep(5)
    # self.driver.find_element(By.XPATH, "//input[@role='textbox']").send_keys(Keys.TAB)
    #
    # self.driver.find_element(By.ID, "ba-banklist-1023").click()
    #
    # try:
    #     element = WebDriverWait(self.driver, 5).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id^="accountname"]'))
    #     )
    #     element.click()
    # finally:
    #     print('yay')

    # acc_name = rand_text

    BankAccountPage.Bank_Accounts.Account_name(self, dup_bank_name)
    BankAccountPage.Bank_Accounts.Account_Type(self)

    self.driver.find_element(By.XPATH, '//input[@componentid="accountnumber-1068"]').send_keys('123')
    BankAccountPage.Bank_Accounts.Continue(self)

    # alert = self.driver.find_element_by_link_text('Please enter a unique name').text
    WebDriverWait(self.driver, 5).until(
        EC.alert_is_present((By.XPATH, '//div//div[@role="alert"]')))

    actual = self.driver.find_element_by_xpath('//div[@role="alert"]').text
    expected = 'Please enter a unique Name'
    self.assertEqual(actual, expected)

    # actual_alert_message= self.driver.find_element(By.XPATH, '//div//div[@class="xui-inputmessage--body"]').text
    # expected_alert_message = 'Please enter a unique name'
    # self.assertEquals(alert, expected_alert_message)

    DeleteBankAccount.Delete_Bank_Accounts.Navigate_to_Charts_of_BankAccounts(self)
    DeleteBankAccount.Delete_Bank_Accounts.Search_bank_account(self, dup_bank_name)
    DeleteBankAccount.Delete_Bank_Accounts.Delete_bank_account(self)

    deleteMessage = self.driver.find_element(By.XPATH, Locators.Locators.DeleteConfirmButton).text
    print(deleteMessage)
