import logging
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


logger = logging.getLogger(__name__)


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Open page: {url}")
    def open(self, url):
        logger.info(f"Open url: {url}")
        self.driver.get(url)

    @allure.step("Find element: {locator}")
    def find(self, locator):
        logger.info(f"Find element: {locator}")
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Find elements: {locator}")
    def finds(self, locator):
        logger.info(f"Find elements: {locator}")
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step("Click element: {locator}")
    def click(self, locator):
        logger.info(f"Click element: {locator}")

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

    @allure.step("Type '{text}' into field: {locator}")
    def type(self, locator, text):
        logger.info(f"Type text into: {locator}")

        element = self.find(locator)

        element.clear()
        element.send_keys(text)

    @allure.step("Check visibility of element: {locator}")
    def is_visible(self, locator):
        logger.info(f"Check visibility: {locator}")

        try:
            self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return True

        except TimeoutException:
            logger.error(f"Element not visible: {locator}")
            return False

    @allure.step("Switch to iframe: {locator}")
    def switch_to_frame(self, locator):
        logger.info(f"Switch to iframe: {locator}")

        iframe = self.find(locator)
        self.driver.switch_to.frame(iframe)

    @allure.step("Switch to default content")
    def switch_to_default(self):
        logger.info("Switch to default content")

        self.driver.switch_to.default_content()

    @allure.step("Scroll to element: {locator}")
    def scroll_to(self, locator):
        logger.info(f"Scroll to element: {locator}")

        element = self.find(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )