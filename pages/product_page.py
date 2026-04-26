import logging
import allure

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import product_page_locators as loc


class ProductPage(BasePage):
    PAGE_URL = '/customizable-desk-9?category=1#attr=1,3'

    def check_name(self):
        logging.info('Проверяем, что у товара есть название')
        with allure.step(f'Проверяем, что у товара есть название'):
            actual_name = self.find(loc.name_product_loc)
            assert len(actual_name.text) > 2, f'Имя товара пустое или меньше 2 символов'

    def check_price(self):
        logging.info('Проверяем, что у товара есть цена')
        with allure.step('Проверяем, что у товара есть цена'):
            actual_price = self.find(loc.price_product_loc).text
            currency, price = actual_price.split(' ')
            assert currency == '$', 'Цена товара не в долларах'
            try:
                assert float(price) > 0, 'Цена товара меньше или равно нулю'
            except ValueError:
                assert False, f'В поле цены не число: {price}'

    def check_price_euro(self):
        logging.info('Проверяем, что у товара есть цена')
        with allure.step('Проверяем, что у товара есть цена'):
            actual_price = self.find(loc.price_product_loc).text
            price, currency = actual_price.split(' ')
            assert currency == '€', 'Цена товара не в евро'
            try:
                assert float(price) > 0, 'Цена товара меньше или равно нулю'
            except ValueError:
                assert False, f'В поле цены не число: {price}'

    def check_image(self):
        logging.info('Проверяем наличие изображения товара')
        with allure.step('Проверяем наличие изображения товара'):
            image_product = self.wait.until(EC.visibility_of_element_located(loc.image_product_loc))
            src = image_product.get_attribute("src")
            assert src, "Атрибут src отсутствует или пуст"

    def add_plus_one(self):
        logging.info('Увеличиваем количество товара на 1')
        with allure.step('Увеличиваем количество товара в корзине на 1'):
            self.find(loc.add_one).click()

    def add_to_cart(self):
        logging.info('Добавляем товар в корзину')
        with allure.step('Нажимаем кнопку "Add to cart"'):
            self.find(loc.add_to_cart).click()

    def verify_added_to_cart_notification(self, expected_count, expected_name):
        logging.info(f'Проверяем уведомление о добавлении в корзину')
        with allure.step(f'Проверяем уведомление о добавлении в корзину'):
            product_in_cart_notification = self.wait.until(EC.visibility_of_element_located(loc.product_name_in_cart_loc)).text
            count, actual_name = product_in_cart_notification.split(' x ')
            assert int(count) == expected_count, f'Ожидалось количество: {expected_count} \n' \
                                            f'Текущее количество: {count}'
            assert expected_name in actual_name, f'Ожидалось: {expected_name} \n' \
                                                                       f'Текущее: {actual_name}'

    def change_currency_to_euro(self):
        logging.info('Меняем валюту на евро')
        with allure.step('Переключаем валюту на евро'):
            currency = self.find(loc.currency_loc)
            currency.click()
            eur = self.wait.until(EC.element_to_be_clickable(loc.eur_loc))
            eur.click()

    def check_material_legs_is_aluminium(self):
        logging.info('Проверяем, что у товара есть выбор материала ножек из аллюминия')
        with allure.step('Проверяем, что у товара есть выбор материала ножек из аллюминия'):
            materials_legs = self.wait.until(EC.visibility_of_element_located(loc.materials_legs_loc))
            assert 'Aluminium' in materials_legs.text

    def get_prod_name(self):
        logging.info('Получаем название товара')
        with allure.step(f'Получаем название товара'):
            prod_name = self.find(loc.name_product_loc)
            return prod_name.text
