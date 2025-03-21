from data import Data
import pytest
import allure
from pages.home_page import HomePage
from urls import Urls

@pytest.mark.home_page
class TestHomePage:

        @pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, 7])
        @allure.title('Проверка клика на вопрос и получения ответа')
        def test_check_click_question(self, driver, number):
            home_page = HomePage(driver)
            home_page.open(Urls.BASE_URL)
            actual_text = home_page.get_answer_text_on_home_page(number)
            expected_text = Data.EXPECTED_ANSWERS.get(number)

            assert actual_text == expected_text, f"Ожидался текст: '{actual_text}', но получен: '{expected_text}'"