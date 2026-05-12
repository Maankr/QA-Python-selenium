from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def is_loaded(self):
        return (
            self.is_visible(LoginLocators.EMAIL) and
            self.is_visible(LoginLocators.PASSWORD)
        )