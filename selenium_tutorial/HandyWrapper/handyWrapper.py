from selenium import webdriver
from selenium.webdriver.common.by import By


class HandyWrapper():

    # if variable need to be used from Outside for other files in other Methods, __init__ is needed.
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        self.locatorType = locatorType.lower()
        if locatorType == 'ID':
            return By.ID
        elif locatorType == 'NAME':
            return By.NAME
        elif locatorType == 'XPATH':
            return By.XPATH
        else:
            print("Wrong Element Type entered")
        return False


    def getElement(self, webElement, locatorType='id'): #parm must be in that order
        self.locatorType = locatorType.lower()
        getBy = self.getByType(locatorType)
        element = self.driver.find_element(getBy, webElement)
        return element

    def isElementPresent(self, webElement, locatorType):
        if self.getElement(webElement, locatorType) is not None:
            print("Element found")
            return True

        else: print("Element not found")
        return False










