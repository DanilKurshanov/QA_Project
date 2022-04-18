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

    # def should_be_message_about_product_in_basket(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_correc_prise_product_in_backets(self):
        assert self.is_prise_correct(*ProductPageLocators.PRICE_PRODUCTS_IN_BASKET, *ProductPageLocators.PRICE_OF_PRODUCT), ""