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
# from waits.Explicit_wait_type import Explicit_wait
# import HW class from external source
from selenium_tutorial.handyWrapper import HandyWrapper


class run_chrome():

    def usingWrapper(self):
        options = Options()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        # action = ActionChains(driver)
        driver.get("https://www.letskodeit.com/home")
        driverURL = driver.current_url
        # driver.implicitly_wait(10)
        print(driverURL)
        print(driver.title)
        # import class
        HW = HandyWrapper(driver)

        # email = HW.isElementPresent("//*[@id='email']", "XPATH")

        all_courses_link = HW.getElement("//div[@id='navbar-inverse-collapse']/ul/li[2]/a", "XPATH")
        all_courses_link.click()
        print(driver.title)

        element1 = "//div[contains(@class, 'zen-course-list')]//h4[contains(text(), '{0}')]"
        _2ndCourse = element1.format("JavaScript for beginners")
        _2ndCourse_format = HW.getElement(_2ndCourse, "XPATH")
        _2ndCourse_format.click()
        print(driver.title)
        time.sleep(2)




rr = run_chrome()
rr.usingWrapper()










