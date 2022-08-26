from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.ie.service import Service as IEService
#from webdriver_manager.microsoft import IEDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common import by

#driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com")
driver.set_page_load_timeout(10)
driver.find_element(by ="id", value="L2AGLb").click()
driver.find_element(by ="name", value="q").send_keys("test")
SearchButton = driver.find_element(by ="xpath", value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
SearchButton.click()

time.sleep(10)