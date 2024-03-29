from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Login url is not correct'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        EMAIL = self.browser.find_element(*LoginPageLocators.EMAIL)
        EMAIL.send_keys(email)
        PASSWORD1 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        PASSWORD1.send_keys(password)
        PASSWORD2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        PASSWORD2.send_keys(password)
        REGISTER = self.browser.find_element(*LoginPageLocators.REGISTER)
        REGISTER.click()
