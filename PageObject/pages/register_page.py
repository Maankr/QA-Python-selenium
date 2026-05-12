from pages.base_page import BasePage
from locators.register_locators import RegisterLocators


class RegisterPage(BasePage):

    def register(self, firstname, lastname, email, password):

        self.type(RegisterLocators.FIRSTNAME, firstname)
        self.type(RegisterLocators.LASTNAME, lastname)
        self.type(RegisterLocators.EMAIL, email)
        self.type(RegisterLocators.PASSWORD, password)

        self.scroll_to(RegisterLocators.GDPR_CHECKBOX)

        # отмечаем чекбоксы обязательные при регистрации, без них регистрация не проходит
        self._check_checkbox(RegisterLocators.GDPR_CHECKBOX)
        self._check_checkbox(RegisterLocators.CUSTOMER_PRIVACY_CHECKBOX)

        self.click(RegisterLocators.SUBMIT)

    def _check_checkbox(self, locator):
        self.click(locator)

    def is_registration_successful(self):
        return (
                self.is_visible(RegisterLocators.USER_NAME) and
                self.is_visible(RegisterLocators.SIGN_OUT_BUTTON)
        )
