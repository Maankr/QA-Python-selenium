from selenium.webdriver.common.by import By


class CatalogLocators:
    PRODUCTS = (By.ID, "products")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".product-miniature")
    FILTERS = (By.ID, "search_filters")
    PAGINATION = (By.CLASS_NAME, "pagination")
    TOTAL = (By.CSS_SELECTOR, ".total-products")