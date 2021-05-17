from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), \
            'There are products in basket, but should not be'

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), \
            "Basket notification is not presented"
