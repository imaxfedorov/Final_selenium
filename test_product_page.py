from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
import time
import pytest

@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
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

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_adding_button()
    NAME = page.get_product_name()
    PRICE = page.get_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    page.should_be_basket_name()
    page.should_be_basket_price()
    page.compare_price(PRICE)
    page.compare_name(NAME)


@pytest.mark.xfail
def test_message_dissapeared_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
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
    page.should_dissapear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty_basket()
    cart_page.should_not_be_product()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_adding_button()
    page.should_not_be_success_message()
    NAME = page.get_product_name()
    PRICE = page.get_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_basket_name()
    page.should_be_basket_price()
    page.compare_price(PRICE)
    page.compare_name(NAME)

class  TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, 'qszwaxAS28!!')

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_authorized_user()
        page.should_be_adding_button()
        page.should_not_be_success_message()
        NAME = page.get_product_name()
        PRICE = page.get_product_price()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_basket_name()
        page.should_be_basket_price()
        page.compare_price(PRICE)
        page.compare_name(NAME)

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_authorized_user()
        page.should_be_adding_button()
        NAME = page.get_product_name()
        PRICE = page.get_product_price()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_basket_name()
        page.should_be_basket_price()
        page.compare_price(PRICE)
        page.compare_name(NAME)
