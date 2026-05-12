from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

from locators.home_locators import HomeLocators
from locators.catalog_locators import CatalogLocators
from locators.product_locators import ProductLocators
from locators.login_locators import LoginLocators
from locators.register_locators import RegisterLocators


def test_home_page(driver, base_url):
    page = HomePage(driver)
    page.open(base_url)

    elements = [
        HomeLocators.HEADER,
        HomeLocators.SEARCH,
        HomeLocators.PRODUCTS,
        HomeLocators.CART,
        HomeLocators.LOGO,
    ]

    for el in elements:
        assert page.is_visible(el), f"{el} not visible on home page"


def test_catalog_page(driver, base_url):
    page = HomePage(driver)
    page.open(base_url + "2-home")

    elements = [
        CatalogLocators.PRODUCTS,
        CatalogLocators.PRODUCT_ITEMS,
        CatalogLocators.FILTERS,
        CatalogLocators.PAGINATION,
        CatalogLocators.TOTAL,
    ]

    for el in elements:
        assert page.is_visible(el), f"{el} not visible on catalog page"


def test_product_page(driver, base_url):
    page = ProductPage(driver)
    page.open(base_url + "men/1-hummingbird-printed-t-shirt.html")

    elements = [
        ProductLocators.ADD_TO_CART_FORM,
        ProductLocators.QTY,
        ProductLocators.PRICE,
        ProductLocators.TITLE,
        ProductLocators.MAIN,
    ]

    for el in elements:
        assert page.is_visible(el), f"{el} not visible on product page"


def test_login_page(driver, base_url):
    page = LoginPage(driver)
    page.open(base_url + "login")

    elements = [
        LoginLocators.EMAIL,
        LoginLocators.PASSWORD,
        LoginLocators.SUBMIT,
        LoginLocators.FORM,
        LoginLocators.NO_ACCOUNT,
        LoginLocators.LINK,
    ]

    for el in elements:
        assert page.is_visible(el), f"{el} not visible on login page"


def test_register_page(driver, base_url):
    page = RegisterPage(driver)
    page.open(base_url + "registration")

    elements = [
        RegisterLocators.FORM,
        RegisterLocators.FIRSTNAME,
        RegisterLocators.LASTNAME,
        RegisterLocators.EMAIL,
        RegisterLocators.PASSWORD,
    ]

    for el in elements:
        assert page.is_visible(el), f"{el} not visible on register page"