from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    register_email =
    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), \
            'No email-field on page'
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(self.email)
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD1), \
            'No password1-field on page'
        password1_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password1_field.send_keys(self.password)
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD2), \
            'No password2-field on page'
        password2_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        password2_field.send_keys(self.password)
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), \
            'No register-button on page'
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Incorrect url for login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'No login form on page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'No register form on page'
