# Chapter 112
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class SeleniumDriver():
    def __init__(self, driver):
        self.driver = driver

    # getByType is universal attribute to find element by
    def getByType(self, locatorType):
        webLocator = locatorType.lower()
        if webLocator == "ID":
            return By.ID
        elif webLocator == "XPATH":
            return By.XPATH
        elif webLocator == "LINK_TEXT":
            return By.LINK_TEXT
        elif webLocator == "NAME":
            return By.NAME
        else:
            print("Locator is not supported")
        return False

    # prompts for Locator otherwise, default is "id"
    def findElement(self, locator, webLocator="id"):
        try:
            byType = self.getByType(webLocator)
            element = self.driver.find_element(byType, locator)
            print("Element is found")
        except:
            print("Element was not found")
            print_stack()

    def ElementClick(self, locator, locatorType="id"):
        try:
            element = self.driver.findElement(locatorType, locator)
            element.click()
            print("Element is found")

        except:
            print("Element was not clicked because not found")
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.driver.findElement(locatorType, locator)
            element.send_keys(data)
            print("Element is found, string inserter")
        except:
            print("Element was not found")
            print_stack()

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximus: " + str(timeout) + "seconds for elements to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=
            [NoSuchElementException, ElementNotVisibleException])

            element = wait.until(EC.element_to_be_clickable((byType, "//*[@text()='Sign In']")))
            print("Element appeared on the web page")
        except:
            print("no element returned")
            print_stack()
        return element

    def
