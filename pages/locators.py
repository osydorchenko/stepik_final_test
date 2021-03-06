from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")
    PRODUCT_NAME_ADDED = (By.CSS_SELECTOR, "#messages .alert-safe:first-child .alertinner strong")
    PRODUCT_PRICE_ADDED = (By.CSS_SELECTOR, "#messages .alert-safe:last-child .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default:first-child")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, "#messages .alert-safe:first-child .alertinner")
