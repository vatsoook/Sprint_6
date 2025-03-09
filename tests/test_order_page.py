import helper
import pytest
import allure
from pages.order_page import OrderPage
from pages.home_page import HomePage
import urls
@pytest.mark.order_page
class TestOrderPage:

    @allure.title("Заказ самоката через кнопку 'Заказать' в вверху страницы с переходом на главную страницу" )
    def test_order_scooter_button_top_page(self, driver):
        order_page = OrderPage(driver)
        order_page.open(urls.URLS.get('BASE_URL'))
        order_page.check_click_button_top_page()
        actual_order_message = order_page.create_order(*helper.ORDER_CASE_1)

        assert 'Заказ оформлен' in actual_order_message, 'Order creation failed'

        order_page.check_click_view_status()
        order_page.check_click_button_scooter()

        assert driver.current_url == urls.URLS.get('BASE_URL'), 'URL does not match the expected base URL'

    @allure.title("Заказ самоката через кнопку 'Заказать' в вверху страницы с переходом на главную страницу Дзен")
    def test_order_scooter_button_bottom_page(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.URLS.get('BASE_URL'))
        home_page.check_click_button_bottom_page()
        order_page = OrderPage(driver)
        actual_order_message = order_page.create_order(*helper.ORDER_CASE_2)

        assert 'Заказ оформлен' in actual_order_message, 'Order creation failed'

        order_page.check_click_view_status()
        order_page.click_on_the_yandex_logo_and_switch_window()
        current_url = order_page.get_current_url()
        expected_url = urls.URLS.get('DZEN_URL')

        assert current_url == expected_url, f"Ожидался URL: {expected_url}, но получен: {current_url}"