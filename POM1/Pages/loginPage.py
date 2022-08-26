from Locator.Locators import Locators
class LoginPage():
        
    '''create a contructor'''
    '''All the locators below'''
    def __init__(self,driver):
        self.driver = driver
        self.consent_id = Locators.consent_id
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id
        
    '''All the methods below'''          
        
        
    def accept_cookie(self):
         self.driver.find_element(by="id", value = self.consent_id).click()
    
    def enter_username(self,username):
        #self.driver.find_element(by="id", value = self.username_textbox_id).clear()
        self.driver.find_element(by="id", value = self.username_textbox_id).send_keys(username)
    
    def enter_password(self,password):
         #self.driver.find_element(by="id", value = self.username_textbox_id).clear()'''
         self.driver.find_element(by="id", value = self.password_textbox_id).send_keys(password)
         
         
    def click_login(self):
         self.driver.find_element(by="id", value = self.login_button_id).click()