from selenium.webdriver.common.by import By

from TestProjectXero.Demo.Locators import Locators


class Login(object):

    def __init__( self, driver ):
        self.driver = driver

    def Email( self, email ):
        self.driver.find_element(By.XPATH, Locators.Locators.Username).send_keys(email)

    def Password( self, password ):
        self.driver.find_element(By.XPATH, Locators.Locators.Password).clear()
        self.driver.find_element(By.XPATH, Locators.Locators.Password).send_keys(password)

    def SignIn( self ):
        self.driver.find_element(By.XPATH, Locators.Locators.SignIn).click()
