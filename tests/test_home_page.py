from pages.home_page import HomePage


def test_home_page(driver, base_url):
    home = HomePage(driver)
    home.open(base_url)

    prices = home.get_prices()

    assert prices, "Prices are not displayed on home page"