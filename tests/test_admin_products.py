import random
import allure

from pages.admin_products_page import AdminProductsPage


@allure.title("Тест добавления нового продукта")
def test_add_product(driver, base_url, admin_login):

    products = AdminProductsPage(driver)
    products.open_products_page()
    name = f"TestProduct{random.randint(1, 1000)}"
    products.add_product(name)

    assert products.is_product_added()



@allure.title("Тест удаления продукта")
def test_delete_product(driver, base_url, admin_login):

    products = AdminProductsPage(driver)
    products.open_products_page()
    products.delete_selected_product()
    assert products.is_product_deleted()