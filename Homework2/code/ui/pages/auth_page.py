from selenium.webdriver.remote.webelement import WebElement
from ui.pages.base_page import BasePage
from ui.locators.basic_locators import AuthLocators


class AuthPage(BasePage):
    locators = AuthLocators()
    URL = 'https://target.my.com/'

    def __init__(self, driver):
        self.driver = driver

    def login(self, login, password) -> WebElement:
        self.click(self.locators.LOG_IN)
        self.input(self.locators.EMAIl, login)
        self.input(self.locators.PASSWORD, password)
        return self.click(self.locators.LOGIN_ENTER)
