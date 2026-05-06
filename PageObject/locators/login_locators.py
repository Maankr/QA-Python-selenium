from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL = (By.ID, "field-email")
    PASSWORD = (By.ID, "field-password")
    FORM = (By.CLASS_NAME, "login-form")
    NO_ACCOUNT = (By.CLASS_NAME, "no-account")
    LINK = (By.LINK_TEXT, "No account? Create one here")
    SUBMIT = (By.ID, "submit-login")