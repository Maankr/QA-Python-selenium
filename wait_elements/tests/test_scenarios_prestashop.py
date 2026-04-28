import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait(driver):
    return WebDriverWait(driver, 7)


def test_admin_login_logout(driver, base_url):
    driver.get(base_url + "administration")
    w = wait(driver)

    w.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("admin@example.com")
    driver.find_element(By.ID, "passwd").send_keys("Admin123!")
    driver.find_element(By.NAME, "submitLogin").click()

    assert w.until(EC.visibility_of_element_located((By.ID, "main")))

    driver.get(base_url + "administration/index.php?controller=AdminLogin&logout=1")

    assert w.until(EC.visibility_of_element_located((By.ID, "email")))


def test_add_to_cart(driver, base_url):
    driver.get(base_url)
    w = wait(driver)

    products = w.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-miniature")))
    product = random.choice(products)

    product.find_element(By.CSS_SELECTOR, "a").click()

    w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart"))).click()

    assert w.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-products-count")))


def test_currency_home(driver, base_url):
    driver.get(base_url)
    w = wait(driver)

    prices_before = [p.text for p in w.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price"))
    )]

    w.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".currency-selector button")
    )).click()

    currencies = w.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".currency-selector .dropdown-item")
        )
    )

    for c in currencies:
        parent = c.find_element(By.XPATH, "..")
        if "current" not in parent.get_attribute("class"):
            driver.execute_script("arguments[0].click();", c)
            break

    prices_after = [p.text for p in w.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price"))
    )]

    assert prices_before != prices_after


def test_currency_catalog(driver, base_url):
    driver.get(base_url + "2-home")
    w = wait(driver)

    prices_before = [
        p.text for p in driver.find_elements(By.CLASS_NAME, "price")
    ]

    driver.find_element(By.CSS_SELECTOR, ".currency-selector button").click()

    currency = w.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".currency-selector li:not(.current) a")
        )
    )
    currency.click()

    prices_after = [
        p.text for p in driver.find_elements(By.CLASS_NAME, "price")
    ]

    assert prices_before != prices_after