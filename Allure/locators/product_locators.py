from selenium.webdriver.common.by import By


class ProductLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, "button.add-to-cart")
    CART = (By.CLASS_NAME, "cart-products-count")
    TITLE = (By.CSS_SELECTOR, "h1")
    ADD_TO_CART_FORM = (By.ID, "add-to-cart-or-refresh")
    QTY = (By.NAME, "qty")
    PRICE = (By.CLASS_NAME, "current-price")
    MAIN = (By.ID, "main")