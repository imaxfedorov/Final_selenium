from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_adding_button()
    NAME = page.get_product_name()
    PRICE = page.get_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_basket_name()
    page.should_be_basket_price()
    page.compare_price(PRICE)
    page.compare_name(NAME)
