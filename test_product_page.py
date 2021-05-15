from .pages.product_page import PageObject


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = PageObject(browser, link)
    page.open()
    page.should_be_adding_basket_button()
    page.add_object_to_basket()
    page.should_be_name_in_basket()
    page.check_name_in_basket()
    page.should_be_price_in_basket()
    page.check_price_in_basket()
