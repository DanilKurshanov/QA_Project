from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_url_login_correct(self):
        try:
            driver.switch_to_window(driver.window_handles[0])
            'login' in self.browser.current_url
        except NotCorrectUrl:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True