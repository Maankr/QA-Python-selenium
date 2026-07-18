from selenium.webdriver.common.by import By


class AdminLoginLocators:
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    SUBMIT = (By.NAME, "submitLogin")
    DASHBOARD = (By.ID, "main")

    SIGN_IN = (By.XPATH, "//span[normalize-space()='Sign in']")