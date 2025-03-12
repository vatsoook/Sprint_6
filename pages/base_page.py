import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from urls import Urls

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    @allure.step('Открываем страницу: {url}')
    def open(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def is_on_base_url(self):
        return self.driver.current_url == Urls.BASE_URL

    def is_at_dzen_url(self):
        return self.driver.current_url == Urls.DZEN_URL


    def scroll_to_element(self, locator):
        web_element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

        return self.driver.execute_script("arguments[0].scrollIntoView();", web_element)


    @allure.step('Нажимаем кнопку заказать вверху страницы')
    def check_click_button_top_page(self):

        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(BasePageLocators.BUTTON_ORDER_TOP_OF_THE_PAGE)
        )
        button.click()


    @allure.step('Нажимаем на логотип "Яндекс". Переходим в новое окно браузера')
    def click_on_the_yandex_logo_and_switch_window(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(BasePageLocators.BUTTON_LINK_YANDEX)).click()

        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])
        return WebDriverWait(self.driver, timeout=20).until(EC.url_to_be(Urls.BASE_URL))


    @allure.step('Нажать на  кнопку "Самокат ')
    def check_click_button_scooter(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(BasePageLocators.BUTTON_LINK_SCOOTER)).click()

    @allure.step('Ожидание элемента видимости')
    def wait_for_element_visibility(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Клик на элемент {locator}')
    def click_element(self, locator):
        self.wait_for_element_visibility(locator).click()

    @allure.step('Получаем текст элемента {locator}')
    def get_element_text(self, locator):
        return self.wait_for_element_visibility(locator).text