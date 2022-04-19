from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):

    def should_be_basket_page_url(self):
        assert "/basket/" in self.browser.current_url, "URL shoud contains login."

    def is_empty_basket(self):
        assert len(self.browser.find_elements(*BasketPageLocators.EMPTY_BASKET)) == 1, 'Basket is not empty'

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket is not empty, but should be'