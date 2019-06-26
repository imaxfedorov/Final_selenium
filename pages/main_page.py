from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link.click()

    def go_to_login_page(browser):
        link = browser.find_element_by_css_selector("#login_link")
        link.click()