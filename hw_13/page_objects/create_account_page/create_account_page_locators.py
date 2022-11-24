from selenium.webdriver.common.by import By

from hw_13.utilities.web_ui.locator import Locator


class CreateAccountLocators:
    def __init__(self):
        self.__account_create_title = Locator(method=By.XPATH, locator='//div[@class="account-create"]')
        self.__back_to_login = Locator(method=By.XPATH, locator='//a[@class="back-link"]')
        self.__login_page_title = Locator(method=By.XPATH, locator='//div[@class="account-login clearer"]/div/h1')

    @property
    def account_create_title(self):
        return self.__account_create_title.get_locator()

    @property
    def back_to_login(self):
        return self.__back_to_login.get_locator()

    @property
    def login_page_title(self):
        return self.__login_page_title.get_locator()
