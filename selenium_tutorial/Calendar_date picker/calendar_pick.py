
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
from selenium_tutorial.handyWrapper import handyWrapper
from waits.Explicit_wait_type import Explicit_wait

class run_chrome():

    def runTest(self):
        options = Options()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        action = ActionChains(driver)
        driver.get("https://www.goibibo.com/flights/")
        #HW = handyWrapper(driver)
        #EW = Explicit_wait
        # driver.get("http://omayo.blogspot.com")
        driverURL = driver.current_url
        print(driverURL)
        print(driver.title)

        partial_text = "DEL"
        full_text = "New Delhi, India (DEL)"

        entry = driver.find_element(By.XPATH, "//input[@type='text']")
        entry.send_keys(partial_text)
        time.sleep(2)
        suggestedList = driver.find_elements(By.ID, "#autoSuggest-list")


        for element in suggestedList:
            if full_text in element.text:
                print(element.text)
                element.click()
                break






rr = run_chrome()
rr.runTest()







