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
# from selenium_tutorial.handyWrapper import handyWrapper
# from waits.Explicit_wait_type import Explicit_wait

class run_chrome():

    def runTest(self):
        options = Options()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        action = ActionChains(driver)
        driver.get("https://omayo.blogspot.com/#")
        driverURL = driver.current_url
        driver.implicitly_wait(10)
        print(driverURL)
        print(driver.title)

        # identify button
        mouse_button = driver.find_element(By.XPATH, '//*[@id="alert1"]')
        # move mouse to button
        # action.move_to_element(mouse_button).perform()
        # Click on reload
        #reload = driver.find_element(By.XPATH, "//*[@id='mouse-hover-example-div']/div[1]/fieldset/div/div/a[2]")
        # reload.click()







rr = run_chrome()
rr.runTest()
