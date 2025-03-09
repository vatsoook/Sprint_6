import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def scroll_to_questions(self):

        element = self.driver.find_element(*HomePageLocators.TEXT_QUESTION_ABOUT_IMPORTANT)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(HomePageLocators.TEXT_QUESTION_ABOUT_IMPORTANT))

    @allure.step('Получаем текст ответа в соответствии с номером вопроса {question_number} на главной странице')
    def get_answer_text_on_home_page(self, question_number):

            button_question_locator = getattr(HomePageLocators, f'BUTTON_QUESTION_{question_number}')
            label_answer_locator = getattr(HomePageLocators, f'TEXT_ANSWER_{question_number}')

            self.scroll_to_questions()
            self.driver.find_element(*button_question_locator).click()
            return self.driver.find_element(*label_answer_locator).text


    @allure.step('Скроллим до кнопки "Заказать"')
    def scroll_to_order_button(self):
        self.scroll_to_element(HomePageLocators.BUTTON_ORDER_BUTTON_OF_THE_PAGE)

    @allure.step('Скроллим до кнопки "Заказать" и нажимаем кнопку')
    def check_click_button_bottom_page(self):
        element = self.driver.find_element(*HomePageLocators.BUTTON_ORDER_BUTTON_OF_THE_PAGE)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(HomePageLocators.BUTTON_ORDER_BUTTON_OF_THE_PAGE)).click()