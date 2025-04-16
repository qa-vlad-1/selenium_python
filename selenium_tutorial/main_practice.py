# Memorize this Structure
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as Chrome_service

class runChrome()
    def test(self):
        # options = Options()
        # options.headless = True
        chrome_service = Chrome_Service(executable_path="/Users/vladimirkalmykov/Downloads/chromedriver")
        driver = webdriver.Chrome(service=chrome_service)
        # driver = webdriver.Chrome(options=options)
        # Maximizing the Window - for all elements to Display
        driver.maximize_window()
        driver.get("https://www.letskodeit.com/practice")
        driverURL = driver.current_url
        print(driverURL)
        # Looks for Elements, if Not Found, allows 10 seconds for all elements to Load on Page
        driver.implicitly_wait(10)






















        baseURL = 'http://www.expedia.com'
        chrome_service = Chrome_service(executable_path="/Users/vladimirkalmykov/Downloads/chromedriver")
        driver = webdriver.Chrome(service=chrome_service)
        driver.maximize_window()
        driver.get(baseURL)
        current_driver = driver.current_url
        print(current_driver)
        driver.implicitly_wait(10)

#import time
#from selenium import webdriver
#from selenium.webdriver.chrome.service import service as Chrome_service
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.by import By

