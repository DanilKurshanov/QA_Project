from .pages.product_page import ProductPage


def test_can_add_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()

    page.click_on_btn_add_to_basket() # добавление в корзину товара
    page.solve_quiz_and_get_code()

    page.should_be_correc_prise_product_in_backets()