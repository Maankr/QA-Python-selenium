from pages.base_page import BasePage
from locators.home_locators import HomeLocators

class HomePage(BasePage):

    def get_prices(self):
        return [p.text for p in self.finds(HomeLocators.PRICES)]

    def change_currency(self):
        self.click(HomeLocators.CURRENCY_BTN)
        currencies = self.finds(HomeLocators.CURRENCIES)
        currencies[1].click()

    def open_first_product(self):
        self.finds(HomeLocators.PRODUCTS)[0].click()