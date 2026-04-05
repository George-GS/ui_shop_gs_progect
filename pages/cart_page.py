import logging

import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import cart_locators as loc


class CartPage(BasePage):
    PAGE_URL = '/cart'

    def check_product_in_cart(self, product_name):
        logging.info('АААА')
        with allure.step('АААА'):
            self.wait.until(EC.text_to_be_present_in_element(loc.product_in_cart, product_name))
            product_in_cart = self.find(loc.product_in_cart)
            assert product_name in product_in_cart.text

    def check_cart_header(self):
        logging.info('АААА')
        with allure.step('АААА'):
            cart_header = self.find(loc.cart_header)
            assert cart_header.text == 'Order overview', 'Нет заголовка "Order overview"'

    def check_cart_is_empty(self):
        logging.info('АААА')
        with allure.step('АААА'):
            empty_cart_info = self.find(loc.empty_cart_info)
            assert empty_cart_info.text == 'Your cart is empty!', 'Нет информации о том, что корзина пуста'

    def remove_product(self):
        logging.info('АААА')
        with allure.step('АААА'):
            remove_btn = self.find(loc.remove_btn)
            remove_btn.click()
            self.wait.until_not(EC.presence_of_element_located(loc.product_in_cart))








