from pages.home_page import HomePage
import allure

allure.title("Тест смены валюты")
def test_currency_change(driver, base_url):
    home = HomePage(driver)
    home.open(base_url)

    before = home.get_prices()
    home.change_currency()
    after = home.get_prices()

    assert before != after, "Currency did not change"