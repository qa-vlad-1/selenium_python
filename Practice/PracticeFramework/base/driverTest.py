# From PracticeFramework-base - this is practice page

from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from traceback import print_stack

class DriverTestMethod():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        self.locatorType = locatorType.lower()
        if locatorType == "XPATH":
            return By.XPATH
        elif locatorType == "LINK_TEXT":
            return By.LINK_TEXT
        elif locatorType == "ID":
            return By.ID
        elif locatorType == "NAME":
            return By.NAME
        else:
            print("No locator type were found")
        return False

    def findElement(self, locatorType, locator):
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
        except:
            print("no element found")
            print_stack()

    def ElememntClick(self, locatorType, locator):
        try:
            element = self.driver.findElement(locatorType, locator)
            element.click()
        except:
            print("Element is not found")
            print_stack()

    def sendKeys(self, data, locatorType, locator):
        try:
            element = self.driver.find_element(locatorType, locator)
            element.send_keys(data)
        except:
            print("Element is found and text entered")
            print_stack()





