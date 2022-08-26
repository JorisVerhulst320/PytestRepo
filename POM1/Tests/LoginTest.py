from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
import unittest
#to run test from commanLine
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#after load the pages
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
import HtmlTestRunner

class LoginTests(unittest.TestCase):

   @classmethod
   def setUpClass(cls):
       path ="C:/Users/joris.verhulst\OneDrive - Envista/Documents/Chromedriver/chromedriver.exe"
       options = Options()
       options.headless = False
       service = Service(executable_path=path)
       cls.driver = webdriver.Chrome(service=service,options=options)
       cls.driver.implicitly_wait(10)

   def test_login_valid(self):
       driver = self.driver
       self.driver.get("https://test-dtxgo-portal.medicim.local/#/shared-cases?caseId=fe39e017-113a-4939-987f-06cee98d99f7")
       login = LoginPage(driver)
       login.accept_cookie()
       login.enter_username("joris.verhulst2")
       login.enter_password("Tester123#")
       login.click_login()
       time.sleep(5)
       logout = HomePage(driver)
       logout.click_logout()
  
   
        
       
   @classmethod
   def tearDownClass(cls):
    cls.driver.close()
    cls.driver.quit()
    print("Test Completed")
    
    #to run test from command line
if __name__ == '__main__':
       unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/joris.verhulst/eclipse-workspace/POM/Tests'))