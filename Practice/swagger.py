# Execute Test Case from login_page package

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as Chrome_Service
from selenium.webdriver.chrome.options import Options
from Practice.swagger3 import loginPage

class LoginTests():

    def test_validLogin(self):
        options = Options()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        #driver = webdriver.Chrome()
        #driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get('https://www.letskodeit.com/home')
        current_url = driver.current_url
        print(current_url)
        lp = loginPage(driver)

        lp.Login('test@email.com', 'abcabc')






ll = LoginTests()
ll.test_validLogin()

if __name__ == "__main__":
    unittest.main()














