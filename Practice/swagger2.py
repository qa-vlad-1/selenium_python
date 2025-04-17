from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class classOflocators():

    def __init__(self, driver):
        self.driver = driver


    def getByType(self, weblocator):
        self.weblocator = weblocator.lower()
        if weblocator == 'xpath':
            return By.XPATH
        elif weblocator == 'id':
            return By.ID
        elif weblocator == 'name':
            return By.NAME
        elif weblocator == 'linktext':
            return By.LINK_TEXT

    def getLocator(self, weblocator, locatorType):
        try:
            byType = self.getByType(weblocator)
            element = self.driver.find_element(locatorType, weblocator)
        except:
            print("element not found")
            print_stack()


    def getElement(self, locator, locatorType='id'):
        try:
            getByType = self.driver.getLocator(locator, locatorType)

        except:
            print("element not found")
            print_stack()

    def sendKeys(self, data, locator, locatorType='id'):
        try:
            element = self.driver.find_element(locator, locatorType)
            element.click()

        except:
            print("element not found")
            print_stack()

    def ElementClick(self, locator, locatorType='id'):
        try:
            element = self.driver.getElement(locator, locatorType)
            element.click()
        except:
            print("element not found")
            print_stack()










