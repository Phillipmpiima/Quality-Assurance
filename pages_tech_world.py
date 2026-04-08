from selenium.webdriver.common.by  import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self,by,value):
        self.driver.find_element(by,value).click()

    def type(self,by,value,text):
        element=self.driver.find_element(by,value)
        element.send_keys(text)

class LoginPage(BasePage):
    USERNAME =(By.ID,"username")
    PASSWORD =(By.ID,"password")
    LOGIN_BTN =(By.XPATH,"//button[text()='Login']")

    def login(self,username,password):
        self.type(*self.USERNAME,username)
        self.type(*self.PASSWORD,password)
        self.click(*self.LOGIN_BTN)

class Navbar(BasePage):
    CAMERAS_TAB =(By.XPATH,"//nav//button[text()='Cameras']")
    LENSES =(By.XPATH,"//nav//button[text()='Lenses']")
    CONTACT =(By.XPATH,"//nav//button[text()='Contact']")


    def go_to_cameras(self):
        self.click(*self.CAMERAS_TAB)

    def go_to_lenses(self):
        self.click(*self.LENSES)

    def go_to_contact(self):
        self.click(*self.CONTACT)



class ContactPage(BasePage):
    NAME =(By.ID,"name")
    EMAIL =(By.ID,"email")
    TELEPHONE = (By.ID,"phone")
    MESSAGE = (By.ID,"message")
    SUBMIT = (By.XPATH,"//section//button[text()='Send Message']")


    def fill_form(self,name,email,telephone,message):
        self.type(*self.NAME,name)
        self.type(*self.EMAIL,email)
        self.type(*self.TELEPHONE,telephone)
        self.type(*self.MESSAGE,message)

    def submit(self):
        self.click(*self.SUBMIT)

class LogOut(BasePage):
    LOGOUT = (By.CSS_SELECTOR, ".logout")

    def logout(self):
        self.click(*self.LOGOUT)







