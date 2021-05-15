from selenium.webdriver.common.by import By
from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX

class Webdriver_reusable():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver")
    def launchweb(self,URL):
        self.driver.get(URL)
    def closebrowser(self):
        self.driver.close()

