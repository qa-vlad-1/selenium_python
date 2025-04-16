# Actual code to run
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chrome_Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class runChrome():
    def test(self):
        chrome_service = Chrome_Service(executable_path="/Users/vladimirkalmykov/Downloads/chromedriver-123/chromedriver")
        driver = webdriver.Chrome(service=chrome_service)
        driver.maximize_window()
        driver.get("https://www.letskodeit.com/practice")
        driverURL = driver.current_url
        print(driverURL)
        #Looks for Elements, if Not Found, allows 10 seconds for all elements to Load on Page
        # driver.implicitly_wait(3)

        elementText = driver.find_element(By.XPATH, "//div[@id='hide-show-example-div']/fieldset/legend")
        print(elementText.text)

        driver.implicitly_wait(3)

run_tests = runChrome()
run_tests.test()
#=================================================================================
#OR this way, where system path is configured automatic run chromedriver (75)
# import time
# from selenium import webdriver
#
# class run_chrome():
#     def runTest(self):
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#         currentURL = driver.get("https://www.letskodeit.com/practice")
#         print(currentURL)
#         time.sleep(2)
#         driver.implicitly_wait(4)
#
# rr = run_chrome()
# rr.runTest()
