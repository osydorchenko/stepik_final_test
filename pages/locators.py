from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class PageObjectLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    OBJECT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    OBJECT_PRICE = (By.CSS_SELECTOR, ".product_main p")
    OBJECT_NAME_ADDED = (By.CSS_SELECTOR, "#messages .alert-safe:first-child .alertinner strong")
    OBJECT_PRICE_ADDED = (By.CSS_SELECTOR, "#messages .alert-safe:last-child .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
