import pytest
import allure



@allure.title('АААА')
def test_check_product_in_cart(cart_page, product_desk_page, cart_modal_window):
    product_name = 'Customizable Desk'
    product_desk_page.open_page()
    product_desk_page.add_to_cart_hover()
    cart_modal_window.go_to_cart()
    cart_page.check_product_in_cart(product_name)


@allure.title('')
def test_empty_cart(cart_page):
    cart_page.open_page()
    cart_page.check_cart_header()
    cart_page.check_cart_is_empty()


@allure.title('')
def test_remove_product(product_desk_page, cart_modal_window, cart_page):
    product_name = 'Customizable Desk'
    product_desk_page.open_page()
    product_desk_page.add_to_cart_hover()
    cart_modal_window.go_to_cart()
    cart_page.check_product_in_cart(product_name)
    cart_page.remove_product()
    cart_page.check_cart_is_empty()









