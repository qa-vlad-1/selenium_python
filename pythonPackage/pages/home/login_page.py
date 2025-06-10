# page object model = all actions (finding element, clicking, enter text) are performed here, on Login Page (pages)

import time
import unittest

from selenium.webdriver.common.by import By
from pythonPackage.base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    # Helpful if locators change in browser, user quickly modifies them here
    _loginLink = '//*[@id="navbar-inverse-collapse"]/div/div/a'
    _enterEmail = '//input[@tabindex= "4"]'
    _enterPassw = '//input[@name="password"]'
    _loginBtn = '//div/button[@id="login"]'

    # define methods to expose locators
    # now that there is file dedicated to packages to click and send keys (selenium_driver.py),
    # these methods can be comment out
    # def getLoginLink(self):
    #     return self.driver.find_element(By.XPATH, self._loginLink)
    #
    # def getEmailLink(self):
    #     return self.driver.find_element(By.XPATH, self._enterEmail)
    #
    # def getPasswLink(self):
    #     return self.driver.find_element(By.XPATH, self._enterPassw)
    #
    # def getLoginBtnLink(self):
    #     return self.driver.find_element(By.XPATH, self._loginBtn)
    # -----------------
    # now, perform action
    # these coming from base.SeleniumDriver file
    # but they could also come from above methods
    def clickLoginLink(self):
        self.ElementClick(self._loginLink, By.XPATH)
    def enterEmail(self, data, locator, locatorType):
        self.sendKeys(data, self._enterEmail, By.XPATH)
    def enterPassw(self, passw):
        self.sendKeys(passw, self._enterPassw, By.XPATH)
    def clickLoginBtn(self):
        self.ElementClick(self._loginBtn, By.XPATH)

    # Create Test Case
    def Login(self, email, passw):
        self.clickLoginLink()
        self.enterEmail('test@email.com')
        self.enterPassw('abcabc')
        self.clickLoginBtn()















