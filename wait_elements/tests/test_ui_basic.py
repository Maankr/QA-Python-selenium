from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait(driver):
    return WebDriverWait(driver, 7)


def test_home_page(driver, base_url):
    driver.get(base_url)
    w = wait(driver)

    elements = [
        (By.ID, "header"),
        (By.NAME, "s"),
        (By.CSS_SELECTOR, ".product-miniature"),
        (By.ID, "_desktop_cart"),
        (By.CSS_SELECTOR, ".logo"),
    ]

    for e in elements:
        assert w.until(EC.visibility_of_element_located(e))


def test_catalog_page(driver, base_url):
    driver.get(base_url + "2-home")
    w = wait(driver)

    elements = [
        (By.ID, "products"),
        (By.CSS_SELECTOR, ".product-miniature"),
        (By.ID, "search_filters"),
        (By.CLASS_NAME, "pagination"),
        (By.CSS_SELECTOR, ".total-products"),
    ]

    for e in elements:
        assert w.until(EC.visibility_of_element_located(e))


def test_product_page(driver, base_url):
    driver.get(base_url + "men/1-hummingbird-printed-t-shirt.html")
    w = wait(driver)

    elements = [
        (By.ID, "add-to-cart-or-refresh"),
        (By.NAME, "qty"),
        (By.CLASS_NAME, "current-price"),
        (By.CSS_SELECTOR, "h1"),
        (By.ID, "main"),
    ]

    for e in elements:
        assert w.until(EC.visibility_of_element_located(e))

def test_login_page(driver, base_url):
    driver.get(base_url + "login")
    w = wait(driver)

    elements = [
        (By.ID, "field-email"),
        (By.ID, "field-password"),
        (By.ID, "submit-login"),
        (By.CLASS_NAME, "login-form"),
        (By.CLASS_NAME, "no-account"),
        (By.LINK_TEXT, "No account? Create one here"),
    ]

    for e in elements:
        assert w.until(EC.visibility_of_element_located(e))


def test_register_page(driver, base_url):

    driver.get(base_url + "registration")
    w = wait(driver)

    w.until(EC.presence_of_element_located((By.ID, "customer-form")))

    elements = [
        (By.ID, "field-firstname"),
        (By.ID, "field-lastname"),
        (By.ID, "field-email"),
        (By.ID, "field-password"),
    ]

    for e in elements:
        assert w.until(EC.visibility_of_element_located(e))