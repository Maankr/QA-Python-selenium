from pages.admin_login_page import AdminLoginPage
import allure


@allure.title("Тест входа в админку")
def test_admin_login_logout(driver, base_url):
    page = AdminLoginPage(driver)
    page.open(base_url + "administration")

    page.login("admin@example.com", "Admin123!")
    assert page.is_logged_in(), "Login failed"

    page.logout(base_url)
    assert page.is_login_page_visible(), "Logout failed"