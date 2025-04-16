# Chapter 112
from selenium.webdriver.common.by import By

class ElementWrapper():
    def __init__(self, driver):
        self.webdriver = driver

    # getByType is universal attribute to find element by
    def getByType(self, locatorType):
        webLocator = locatorType.lower()
        if webLocator == "id":
            return By.ID
        elif webLocator == "xpath":
            return By.XPATH
        else:
            print("Locator is not supported")
        return False

    # prompts for Locator otherwise, default is "id"
    def findElement(self, locator, webLocator="id"):
        #initializing/declaring element to empty
        element = None
        try:
            byType = self.getByType(webLocator)
            element = self.webdriver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element Not Found")
        return element





