import pytest
from selenium import webdriver

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    yield driver
    driver.quit()