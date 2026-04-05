import logging
import allure

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import folder_product_desk_locators as loc


class FolderProductDeskPage(BasePage):
    PAGE_URL = '/category/desks-1'

    def products_displayed_on_page(self):
        count_product = self.get_visible_products_count_static()
        assert count_product > 0, f'На странице {self.PAGE_URL} нет товаров'

    def search_product(self, product_name):
        logging.info(f'Через поиск ищем товар {product_name}')
        with allure.step(f'Через поиск ищем товар {product_name}'):
            search_field = self.find(loc.search_loc)
            search_field.send_keys(product_name)
            search_field.send_keys(Keys.ENTER)
        return self

    def get_visible_products_count_after_action(self):
        self.wait.until(EC.url_changes(f'{self.BASE_URL}{self.PAGE_URL}'))
        products_count = self.find_all(loc.visible_products_loc)
        return len(products_count)

    def get_visible_products_count_static(self):
        products_count = self.find_all(loc.visible_products_loc)
        return len(products_count)

    def verify_products_count(self, expected_count):
        actual_count = self.get_visible_products_count_after_action()
        assert actual_count == expected_count, \
            f'Ожидалось количество товаров {expected_count}, отображается товаров {actual_count}'
        return self

    def verify_product_in_results(self, product_name):
        product_in_result = self.find(loc.visible_products_loc)
        assert 'Customizable Desk' in product_in_result.text, f'В результатах нет товара {product_name}'

    def check_product_not_exist(self, product_name):
        actual_text_no_result = self.wait.until(EC.presence_of_element_located(loc.no_result)).text
        expected_text_no_result = 'No results'
        actual_text_no_result_with_product = self.wait.until(EC.presence_of_element_located(
            loc.no_result_with_product)).text
        expected_text_no_result_with_product = f'No results for "{product_name}" in category "Desks".'
        assert actual_text_no_result == expected_text_no_result, \
            f'Ожидался текст: {expected_text_no_result}, текущий текст: {actual_text_no_result}'
        assert actual_text_no_result_with_product == expected_text_no_result_with_product, \
            f'Ожидался текст: {expected_text_no_result_with_product}, текущий текст: {actual_text_no_result_with_product}'

    def select_checkbox_filter_aluminium(self):
        self.wait.until(EC.visibility_of_element_located(loc.sss))
        checkbox_filter = self.wait.until(EC.element_to_be_clickable(loc.checkbox_aluminium))
        checkbox_filter.click()

    def add_to_cart_hover(self):
        product_table = self.wait.until(EC.visibility_of_element_located(loc.product_table))
        self.action.move_to_element(product_table).perform()
        self.wait.until(EC.element_to_be_clickable(loc.cart_btn)).click()











