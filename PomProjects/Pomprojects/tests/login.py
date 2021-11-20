import unittest
import time,os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        s = Service("F:/Django_projects/PomProjects/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

        self.driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID,'btnLogin').click()
        self.driver.find_element(By.ID,'welcome').click()
        self.driver.find_element(By.LINK_TEXT,'Logout').click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")