from .Pages.product_page import ProductPage
import pytest
import time


@pytest.mark.parametrize('promo_number', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail),
                                          "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_number):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}'
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.should_be_a_mes_with_title()
    page.should_be_a_mes_with_price()
    page.compare_titles()
    page.compare_prices()


# def test_titles_should_be_compared(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#     page = ProductPage(browser, link)
#     page.open()
#     page.guest_can_add_product_to_basket()
#     page.compare_titles()


# def test_prices_should_be_compared(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#     page = ProductPage(browser, link)
#     page.open()
#     page.guest_can_add_product_to_basket()
#     page.compare_prices()








