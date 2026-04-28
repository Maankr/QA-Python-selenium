import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--base-url", default="http://localhost:8081/")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService())
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")

    yield driver
    driver.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")