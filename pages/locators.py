from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    PASSWORD1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "form#add_to_basket_form > button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "div#messages > div.alert-success > div.alertinner > strong")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, "div#messages > div.alert-info > div.alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages > div.alert-success")

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class CartPageLocators(object):
    EMPTY_FLAG = (By.CSS_SELECTOR, "div.page_inner > div.content > div#content_inner > p")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "div#messages > div.alert-success > div.alertinner > strong")