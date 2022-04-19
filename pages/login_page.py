from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_url_login_correct(), 'Login Url is not correct'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login Register is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.NEW_REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.NEW_REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REPEAT_NEW_REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()






