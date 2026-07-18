import allure

from pages.base_page import BasePage
from locators.admin_products_locators import AdminProductsLocators


class AdminProductsPage(BasePage):

    @allure.step("Open products page")
    def open_products_page(self):

        self.click(AdminProductsLocators.CATALOG)
        self.click(AdminProductsLocators.PRODUCTS)

    @allure.step("Add product: {name}")
    def add_product(self, name):

        self.click(AdminProductsLocators.ADD_PRODUCT)

        self.switch_to_frame(
            AdminProductsLocators.PRODUCT_IFRAME
        )

        self.click(
            AdminProductsLocators.ADD_PRODUCT_ADD
        )

        self.switch_to_default()

        self.type(
            AdminProductsLocators.PRODUCT_NAME,
            name
        )

        self.click(AdminProductsLocators.SAVE)

    @allure.step("Delete product")
    def delete_selected_product(self):

        self.click(AdminProductsLocators.FIND_DELETE)

        self.click(AdminProductsLocators.DELETE)

        self.click(
            AdminProductsLocators.CONFIRM_DELETE
        )

    @allure.step("Check product added")
    def is_product_added(self):

        return self.is_visible(
            AdminProductsLocators.SUCCESS_MESSAGE
        )

    @allure.step("Check product deleted")
    def is_product_deleted(self):

        return self.is_visible(
            AdminProductsLocators.SUCCESS_MESSAGE
        )