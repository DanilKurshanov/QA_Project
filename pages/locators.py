from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LINK_BASKET = (By.CSS_SELECTOR, 'span.btn-group a[class="btn btn-default"]')

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")

    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, 'div.product_main p.price_color')

    PRICE_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")

    ALERT_ADDED_TO_CART_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")

class BasketPageLocators():
    MESSAGE_ABOUT_EMPTY = (By.CSS_SELECTOR, 'div#content_inner p')