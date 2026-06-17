from selenium.webdriver.common.by import By


class RegisterLocators:
    FIRSTNAME = (By.ID, "field-firstname")
    LASTNAME = (By.ID, "field-lastname")
    EMAIL = (By.ID, "field-email")
    PASSWORD = (By.ID, "field-password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")

    GDPR_CHECKBOX = (By.XPATH, "//label[.//input[@name='psgdpr']]")
    CUSTOMER_PRIVACY_CHECKBOX = (By.XPATH, "//label[.//input[@name='customer_privacy']]")

    # для проверки успешно регистрации
    USER_NAME = (By.CSS_SELECTOR, ".user-info .account .hidden-sm-down")
    SIGN_OUT_BUTTON = (By.CSS_SELECTOR, ".user-info .logout")
    FORM = (By.ID, "customer-form")