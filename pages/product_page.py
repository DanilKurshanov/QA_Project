from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET), "Add to basket button not presented"

    def should_be_name_of_product(self):
        assert self.is_element_present(*ProductPageLocators.NAME_OF_PRODUCT), "Name of product don't found"

    def should_be_price_of_product(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_OF_PRODUCT), "Product Price not found"

    def click_on_btn_add_to_basket(self):
        bnt_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        bnt_add_to_basket.click()


    def should_be_correc_product_name_in_alert_messege(self):
        alert_name = self.browser.find_element(*ProductPageLocators.ALERT_ADDED_TO_CART_NAME).text
        name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        assert alert_name == name, "The name in the basket does not match"

    def should_be_correc_prise_product_in_backets(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCTS_IN_BASKET).text
        price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        assert price_of_product == price_in_basket, 'Price in the basket does not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART_NAME), \
            "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_ADDED_TO_CART_NAME)