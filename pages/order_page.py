import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)

    @allure.step('Вводим имя: {name}')
    def check_input_name(self, name):
        self.driver.find_element(*OrderPageLocators.INPUT_NAME).send_keys(name)

    @allure.step('Вводим фамилию: {surname}')
    def check_input_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.INPUT_SURNAME).send_keys(surname)

    @allure.step('Вводим адрес: {address}')
    def check_input_address(self, address):
        self.driver.find_element(*OrderPageLocators.INPUT_ADDRESS).send_keys(address)

    @allure.step('Выбор станцию метро')
    def check_input_station_metro(self):
        self.driver.find_element(*OrderPageLocators.INPUT_METRO_STATION).click()
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(OrderPageLocators.METRO_STATION_PREOBRAZHENSKAYA_SQUARE))
        self.driver.find_element(*OrderPageLocators.METRO_STATION_PREOBRAZHENSKAYA_SQUARE).click()

    @allure.step('Вводим номер телефона: {phone_number}')
    def check_input_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.INPUT_PHONE_NUMBER).send_keys(phone_number)

    @allure.step('Нажимаем кнопку далее')
    def check_click_next(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()

    @allure.step('Выбираем дату')
    def check_click_date(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(OrderPageLocators.INPUT_SELECT_DATE)).click()
        self.driver.find_element(*OrderPageLocators.SELECT_DATE).click()

    @allure.step('Выбираем срок аренды:  {rental_period}')

    def check_rental_period(self, rental_period):

        self.driver.find_element(*OrderPageLocators.INPUT_RENTAL_PERIOD).click()
        match rental_period:
            case 1:
                self.driver.find_element(*OrderPageLocators.SELECT_RENTAL_PERIOD_TWO_DAYS).click()
            case 2:
                self.driver.find_element(*OrderPageLocators.SELECT_RENTAL_PERIOD_FOUR_DAYS).click()


    @allure.step('Выбираем цвет самоката: {color}')

    def check_scooter_color(self, color):
        match color:
            case 'black':
                self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_BLACK).click()
            case 'grey':
                self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_GREY).click()


    @allure.step('Вводим комментарий для курьера: {comment}')
    def check_input_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT_FOR_COURIER).click()
        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT_FOR_COURIER).send_keys(comment)

    @allure.step('Нажимаем кнопку заказать в финале')
    def check_click_next_final(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(OrderPageLocators.BUTTON_ORDER_FINAL)).click()


    @allure.step('Нажимаем кнопку "Да" в финале')
    def check_click_yes_final(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(OrderPageLocators.BUTTON_YES_PLACE_ORDER)).click()


    @allure.step('Нажимаем кнопку "Посмотреть статус" ')
    def check_click_view_status(self):

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.BUTTON_VIEW_STATUS)).click()


    def create_order(self, name, surname, address, phone_number, rental_period, color, comment):
        self.check_input_name(name)
        self.check_input_surname(surname)
        self.check_input_address(address)
        self.check_input_station_metro()
        self.check_input_phone_number(phone_number)
        self.check_click_next()
        self.check_click_date()
        self.check_rental_period(rental_period)
        self.check_scooter_color(color)
        self.check_input_comment(comment)
        self.check_click_next_final()
        self.check_click_yes_final()

        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.TEXT_ORDER_SUBMITTED)).text