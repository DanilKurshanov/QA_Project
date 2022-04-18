import pytest

from .pages.product_page import ProductPage

links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
]

promo_links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                             marks=pytest.mark.xfail),
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

@pytest.mark.parametrize('product', promo_links)
def test_can_add_product_to_basket(browser, product: str) -> None:

    link = product
    page = ProductPage(browser, link)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()

    page.should_be_add_to_basket_button()
    page.should_be_name_of_product()
    page.should_be_price_of_product()

    page.click_on_btn_add_to_basket() # добавление в корзину товара
    page.solve_quiz_and_get_code()

    page.should_be_correc_product_name_in_alert_messege()
    page.should_be_correc_prise_product_in_backets()


@pytest.mark.parametrize('product', links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, product: str) -> None:
    link = product
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()

    page.click_on_btn_add_to_basket()  # добавление в корзину товара
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.parametrize('product', links)
def test_guest_cant_see_success_message(browser, product: str) -> None:
    link = product
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.should_not_be_success_message()

@pytest.mark.parametrize('product', links)
def test_message_disappeared_after_adding_product_to_basket(browser, product: str) -> None:
    link = product
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()

    page.click_on_btn_add_to_basket()  # добавление в корзину товара
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()