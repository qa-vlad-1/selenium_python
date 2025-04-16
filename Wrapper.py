from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chrome_Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class Wrapper():
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == 'XPATH':
            return By.XPATH
        elif locatorType == 'NAME':
            return By.NAME
        elif locatorType == 'LINK_TEXT':
            return By.LINK_TEXT
        else:
            print("Wrong locator used")


    def getElement(self, locator, locatorType='id'):
        element = None
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(locatorType, locator)
            print("Element is found")
        except:
            print("No Such Element")
            return element

    def isElemenetPresent(self, locator, locatorType='id'):
        element = None
        try:
            element = self.driver.find_element(locatorType, locator)
            if element is not None:
                print("Element exist")
                return True
            else:return False
        except:
            print("Element does not exist")
            return False


















