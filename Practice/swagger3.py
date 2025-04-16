
import time
import unittest

from selenium.webdriver.common.by import By

class loginPage():

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    _sign_in = '//*[@id="navbar-inverse-collapse"]/div/div/a'
    _enterEmail = '//input[@tabindex= "4"]'
    _enterPassw = '//input[@name="password"]'
    _login = '//div/button[@id="login"]'


    # create Method
    def getSigninLink(self):
        return self.driver.find_element(By.XPATH, self._login)
    def getEmailLink(self):
        return self.driver.find_element(By.XPATH, self._enterEmail)
    def getPassLink(self):
        return self.driver.find_element(By.XPATH, self._enterPassw)
    def getLoginLink(self):
        return self.driver.find_element(By.XPATH, self._login)

    # create action for method
    def clickSignin(self):
        self.getSigninLink().click()
    def enterEmail(self):
        self.getEmailLink().senk_keys(self._enterEmail)
    def enterPassword(self):
        self.getPassLink().send_keys(self._enterPassw)
    def clickLogin(self):
        self.getLoginLink().click()

    # Test Case
    def Login(self, email, passw):
        self.clickSignin()
        self.enterEmail()
        self.enterPassword()
        self.clickLogin()














