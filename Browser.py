from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time

class scenarioTest():
 def launchweb(self,URL):
   driver=webdriver.Chrome(executable_path="chromedriver")
   driver.get(URL)

 def waitTime(self,timeInput):
   time.sleep(timeInput)