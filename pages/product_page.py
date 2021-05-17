from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_adding_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), 'No button adding to basket on a page'

    def add_object_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_basket.click()
        # self.solve_quiz_and_get_code()

    def check_name_in_basket(self):
        object_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        object_name_added = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED).text
        assert object_name_added == object_name, 'Object name in basket is incorrect'

    def should_be_price_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_ADDED),\
            'No price in basket on a page'

    def check_price_in_basket(self):
        object_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        object_price_added = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ADDED).text
        assert object_price_added == object_price, 'Object price in basket is incorrect'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            'Success message is presented, but should not be'

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            'Success message is not disappeared'

    def should_be_name_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_ADDED),\
            'No object name in basket on a page'
