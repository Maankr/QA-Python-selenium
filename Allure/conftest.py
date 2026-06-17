import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.admin_login_page import AdminLoginPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--base-url", default="http://localhost:8081/")
    parser.addoption("--timeout", default=10, type=int)


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture
def timeout(request):
    return request.config.getoption("--timeout")


@pytest.fixture
def driver(request, timeout):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(
            options=options,
            service=ChromeService()
        )
    else:
        driver = webdriver.Firefox()

    driver.maximize_window()

    driver.implicitly_wait(timeout)

    yield driver
    driver.quit()


@pytest.fixture
def admin_login(driver, base_url):
    page = AdminLoginPage(driver)
    page.open(base_url + "administration")
    page.login("admin@example.com", "Admin123!")
    assert page.is_logged_in()
    return page