
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
from waits.Explicit_wait_type import Explicit_wait
from selenium_tutorial.handyWrapper import handyWrapper
import time

class run_chrome():

    def runTest(self):
        driver = webdriver.Chrome()
        action = ActionChains(driver)
        driver.maximize_window()
        #driver.get("http://omayo.blogspot.com")
        driver.get("https://www.letskodeit.com/practice")
        #driver.get("https://www.goibibo.com/")
        #driver.get('http://southwest.com')
        #HW = handyWrapper(driver)
        currentURL = driver.current_url
        print(currentURL)
        driver.implicitly_wait(5)
        #time.sleep(2)






rr = run_chrome()
rr.runTest()













