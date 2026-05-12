from selenium.webdriver.common.by import By


class AdminProductsLocators:
    CATALOG = (By.ID, "subtab-AdminCatalog")
    PRODUCTS = (By.ID, "subtab-AdminProducts")

    ADD_PRODUCT = (By.ID, "page-header-desc-configuration-add")
    WAIT_PRODUCT_ADD = (By.ID, "modal-create-product")
    ADD_PRODUCT_ADD = (By.ID, "create_product_create")
    PRODUCT_IFRAME = (By.CSS_SELECTOR, "#modal-create-product iframe")
    PRODUCT_NAME = (By.CSS_SELECTOR, "input[name='product[header][name][1]']")
    SAVE = (By.ID, "product_footer_save")

    FIND_DELETE = (By.CSS_SELECTOR, ".dropdown-toggle-dots")
    DELETE = (By.CSS_SELECTOR, ".grid-delete-row-link")
    CONFIRM_DELETE = (By.CSS_SELECTOR, ".btn-confirm-submit")

    # по allert проверка не проходит и не может найти сообщение поэтому тест падает, сделала через XPATH
    SUCCESS_MESSAGE = (By.XPATH, "//div[@role='alert']//p[contains(.,'Successful')]")