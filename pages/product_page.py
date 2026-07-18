from pages.base_page import BasePage
from locators.product_locators import ProductLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        self.click(ProductLocators.ADD_TO_CART)

    def is_added(self):
        return self.is_visible(ProductLocators.CART)

    def is_loaded(self):
        return self.is_visible(ProductLocators.TITLE)
