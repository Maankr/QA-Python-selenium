from pages.base_page import BasePage
from locators.admin_login_locators import AdminLoginLocators


class AdminLoginPage(BasePage):

    def login(self, email, password):
        self.type(AdminLoginLocators.EMAIL, email)
        self.type(AdminLoginLocators.PASSWORD, password)
        self.click(AdminLoginLocators.SUBMIT)

    def is_logged_in(self):
        return self.is_visible(AdminLoginLocators.DASHBOARD)

    def logout(self, base_url):
        self.open(base_url + "index.php?controller=AdminLogin&logout=1")

    def logout_s(self, base_url):
            self.open(base_url + "index.php?controller=AdminLogin&logout=1")

    def is_login_page_visible(self):
        return self.is_visible(AdminLoginLocators.SIGN_IN)