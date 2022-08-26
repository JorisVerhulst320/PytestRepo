from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service 


class Test():
    @pytest.fixture()
    def test_setup(self):
        global driver
        service = Service(executable_path="C:/Users/joris.verhulst\OneDrive - Envista/Documents/Chromedriver/chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(10)
        driver.maximize_window()
        
    def test_login(self,test_setup):
        driver.get("https://test-dtxgo-portal.medicim.local/#/shared-cases?caseId=fe39e017-113a-4939-987f-06cee98d99f7")
        driver.find_element(by="id", value = "acceptCookieConsentButton").click()
        driver.find_element(by="id", value = "Username").send_keys("joris.verhulst2")
        driver.find_element(by="id", value = "Password").send_keys("Tester123#")
        driver.find_element(by="id", value = "btnLogin").click()
      
    def test_logout(self):
        driver.find_element(by="id", value = "lnkNAVIGATION.Logout").click()
        
    def tear_teardown(self):
        driver.close()
        driver.quit()