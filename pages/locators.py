from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")

    PRICE_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "div[class='basket-mini pull-right hidden-xs']")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, 'div.product_main p.price_color')

    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')
    # REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")