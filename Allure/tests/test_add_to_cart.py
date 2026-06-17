from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_add_to_cart(driver, base_url):
    home = HomePage(driver)
    home.open(base_url)

    home.open_first_product()

    product = ProductPage(driver)
    product.add_to_cart()

    assert product.is_added(), "Product was not added to cart"