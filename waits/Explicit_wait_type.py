from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium_tutorial.handyWrapper import handyWrapper
from traceback import print_stack
from selenium.webdriver.common.by import By

class Explicit_wait:

    def __init__(self, driver):
        self.driver = driver
        self.HW = handyWrapper(driver)

    def waitForElement(self, driver, timeout=10, poll_frequency=1):
        element = None
        try:
            wait = WebDriverWait(driver, timeout=timeout , poll_frequency=poll_frequency)
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@text()='Sign In']")))

        except:
            print("no element returned")
        return element








