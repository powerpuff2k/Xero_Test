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
import HtmlTestRunner

words = ['SAVINGS', 'CREDIT', 'COMPANY', 'JOINT', 'CHARITY']
bank_name = random.choice(words)


class Adding_Bank_Account_to_Demo_Org(unittest.TestCase):


##This setup classmethod will run only once before all the test methods. Here its used to login, and capturing the org

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox(executable_path=r"C:/Users/power/Xero_Test/Xero/Drivers/geckodriver-v0.26.0-win64/geckodriver.exe")
        cls.driver.maximize_window()

        cls.driver.get("https://www.xero.com/nz/")
        cls.driver.implicitly_wait(2000)
        cls.driver.find_element(By.XPATH, Locators.Locators.btn_login).click()

        Login.Login.Email(cls, 'powerpuff2k@gmail.com')
        Login.Login.Password(cls, 'password1')
        Login.Login.SignIn(cls)

        cls.driver.implicitly_wait(30)

        # select Org and Go to Bank Account

        Org = cls.driver.find_element_by_class_name(Locators.Locators.Current_Org)
        print(Org.text)
        Org.click()

##This setup self method will run before every test method. Here it is going to the Bank Accounts page, selecting ANZ NZ account
# and filling up the form and submitting it

    def setUp(self) -> None:
        Homepage.Homepage.link_to_Accounting(self)
        Homepage.Homepage.link_to_Bank_Accounts(self)
        Homepage.Homepage.Add_bank_Account_link(self)

        WebDriverWait(self.driver, 10000).until(
            EC.visibility_of_element_located((By.XPATH, '//h1[@class="ba-page-title"]')))

        # Find ANZ (NZ) from the list and go to Account details
        BankAccountPage.Bank_Accounts.Find_your_bank(self, 'ANZ (NZ)')
        time.sleep(2)

        self.driver.find_element(By.XPATH, Locators.Locators.Bank_Name).send_keys(Keys.TAB)

        self.driver.find_element(By.ID, Locators.Locators.Select_Result).click()

        #Add account details - AccountName,AccountType,AccountNumber
        element = WebDriverWait(self.driver, 10000).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.Locators.Acct_Name_Field))
            )
        element.click()

        BankAccountPage.Bank_Accounts.Account_name(self, bank_name)
        BankAccountPage.Bank_Accounts.Account_Type(self)
        time.sleep(2)

        BankAccountPage.Bank_Accounts.Account_number(self, 12345)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,Locators.Locators.Continue_button)))

        BankAccountPage.Bank_Accounts.Continue(self)

#This teardown method will run after every test method. Here it is deleting the bank acccount that is added.

    def tearDown(self) -> None:

        DeleteBankAccount.Delete_Bank_Accounts.Navigate_to_Charts_of_BankAccounts(self)
        DeleteBankAccount.Delete_Bank_Accounts.Search_bank_account(self, bank_name)
        DeleteBankAccount.Delete_Bank_Accounts.Delete_bank_account(self)

        deleteMessage = self.driver.find_element(By.XPATH, Locators.Locators.DeleteConfirmButton).text
        print(deleteMessage)

#Thats the first test case. To verify that bank account is added successfully.
    def test_Adding_New_Bank_Account(self):


        Verify_Bank_Acc_Added = self.driver.find_element(By.XPATH, Locators.Locators.success_message).text
        self.assertEqual(Verify_Bank_Acc_Added, bank_name +' has been added.')


#This is the test case to verify that duplicate account cannot be added. I am adding the same bank name in
# the form for adding the bank account details and verifying that the promt alert is shown.

    def test_Add_Dup_Bank_Account(self):
        print((self.driver.find_element(By.XPATH, Locators.Locators.success_message)).text)

        Homepage.Homepage.link_to_Accounting(self)
        Homepage.Homepage.link_to_Bank_Accounts(self)
        Homepage.Homepage.Add_bank_Account_link(self)

        WebDriverWait(self.driver, 10000).until(
            EC.visibility_of_element_located((By.XPATH, Locators.Locators.page_title)))

        # Find ANZ (NZ) from the list and go to Account details
        BankAccountPage.Bank_Accounts.Find_your_bank(self, 'ANZ (NZ)')
        time.sleep(2)

        self.driver.find_element(By.XPATH, Locators.Locators.Bank_Name).send_keys(Keys.TAB)

        self.driver.find_element(By.ID, Locators.Locators.Select_Result).click()

        #waiting for the Bank accounts page to load

        element = WebDriverWait(self.driver, 10000).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.Locators.Acct_Name_Field))
            )
        element.click()

        #Filling up the form for Bank Account

        BankAccountPage.Bank_Accounts.Account_name(self, bank_name)
        BankAccountPage.Bank_Accounts.Account_Type(self)
        time.sleep(2)

        BankAccountPage.Bank_Accounts.Account_number(self, 12345)

        BankAccountPage.Bank_Accounts.Continue(self)

        #waiting for the prompt alert to appear and then capturing it

        WebDriverWait(self.driver, 5000).until(
            EC.visibility_of_element_located((By.XPATH, Locators.Locators.prompt_alert)))

        alert = self.driver.find_element_by_xpath(Locators.Locators.prompt_alert).text
        self.assertEqual(alert, 'Please enter a unique Name')



    @classmethod
    def tearDownClass(cls) -> None:

        cls.driver.close()
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\power\PycharmProjects\Xero\Reports"))