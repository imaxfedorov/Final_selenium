from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket.click()

    def should_be_adding_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Button is not presented'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return price.text

    def get_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return name.text

    def should_be_basket_price(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE), "Price is not presented"

    def should_be_basket_name(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME), "Name is not presented"

    def compare_price(self, price):
        assert price == self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE).text, "Price is incorrect"


    def compare_name(self, name):
        assert name == self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text, "Name is incorrect"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message isn't dissapear"