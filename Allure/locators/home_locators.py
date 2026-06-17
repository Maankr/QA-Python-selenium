from selenium.webdriver.common.by import By


class HomeLocators:
    PRODUCTS = (By.CSS_SELECTOR, ".product-miniature")
    PRICES = (By.CSS_SELECTOR, ".price")
    CURRENCY_BTN = (By.CSS_SELECTOR, ".currency-selector button")
    CURRENCIES = (By.CSS_SELECTOR, ".currency-selector .dropdown-item")
    CART_COUNT = (By.CLASS_NAME, "cart-products-count")
    HEADER = (By.ID, "header")
    SEARCH = (By.NAME, "s")
    CART = (By.ID, "_desktop_cart")
    LOGO = (By.CSS_SELECTOR, ".logo")
