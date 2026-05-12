import random
from pages.admin_products_page import AdminProductsPage


def test_add_product(driver, base_url, admin_login):
    products = AdminProductsPage(driver)
    products.open_products_page()
    name = f"TestProduct{random.randint(1, 1000)}"
    products.add_product(name)
    assert products.is_product_added(), f"Product {name} was not added"


def test_delete_product(driver, base_url, admin_login):
    products = AdminProductsPage(driver)
    products.open_products_page()
    products.delete_selected_product()
    assert products.is_product_deleted(), "Product was not deleted"