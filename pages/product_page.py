from .base_page import BasePage
from .locators import PageObjectLocators


class PageObject(BasePage):
    def should_be_adding_basket_button(self):
        assert self.is_element_present(*PageObjectLocators.ADD_TO_BASKET), 'No button adding to basket on a page'

    def add_object_to_basket(self):
        button_basket = self.browser.find_element(*PageObjectLocators.ADD_TO_BASKET)
        button_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_name_in_basket(self):
        assert self.is_element_present(*PageObjectLocators.OBJECT_NAME_ADDED), 'No object name in basket on a page'

    def check_name_in_basket(self):
        object_name = self.browser.find_element(*PageObjectLocators.OBJECT_NAME).text
        object_name_added = self.browser.find_element(*PageObjectLocators.OBJECT_NAME_ADDED).text
        assert object_name_added == object_name, 'Object name in basket is incorrect'

    def should_be_price_in_basket(self):
        assert self.is_element_present(*PageObjectLocators.OBJECT_PRICE_ADDED), 'No price in basket on a page'

    def check_price_in_basket(self):
        object_price = self.browser.find_element(*PageObjectLocators.OBJECT_PRICE).text
        object_price_added = self.browser.find_element(*PageObjectLocators.OBJECT_PRICE_ADDED).text
        assert object_price_added == object_price, 'Object price in basket is incorrect'
