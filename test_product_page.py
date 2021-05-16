from .pages.product_page import PageObject
import pytest


@pytest.mark.parametrize('promo_code', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, promo_code):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_code}'
    page = PageObject(browser, link)
    page.open()
    page.should_be_adding_basket_button()
    page.add_object_to_basket()
    page.should_be_name_in_basket()
    page.check_name_in_basket()
    page.should_be_price_in_basket()
    page.check_price_in_basket()
