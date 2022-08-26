from Locator.Locators import Locators
class HomePage():
    
    '''create a contructor'''
    '''All the locators below'''
    def __init__(self,driver):
        self.driver = driver
        self.logout_button_id = "lnkNAVIGATION.Logout"
        
    '''All the methods below'''
        
    def click_logout(self):
        self.driver.find_element(by="id", value = Locators.logout_button_id).click()