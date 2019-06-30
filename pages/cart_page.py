from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .product_page import ProductPage
from .locators import CartPageLocators

class CartPage(BasePage):
    def should_be_empty_basket(self):
        assert 'empty' in self.browser.find_element(*CartPageLocators.EMPTY_FLAG).text, "Basket is not empty"

    def should_not_be_product(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_PRODUCT_NAME), \
            "Product should not be presented"