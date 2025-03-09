from selenium.webdriver.common.by import By

class OrderPageLocators:

    INPUT_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    INPUT_SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    INPUT_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    INPUT_METRO_STATION = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_STATION_PREOBRAZHENSKAYA_SQUARE = (By.XPATH, '//div[contains(text(), "Преображенская площадь")]')
    INPUT_PHONE_NUMBER = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    BUTTON_NEXT= (By.XPATH, '//button[text()="Далее"]')
    INPUT_SELECT_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    SELECT_DATE = (By.XPATH, '//div[@aria-label = "Choose воскресенье, 9-е марта 2025 г."]')
    INPUT_RENTAL_PERIOD = (By.XPATH, '//div[text()="* Срок аренды"]')
    SELECT_RENTAL_PERIOD_TWO_DAYS = (By.XPATH, '//div[text()="сутки"]')
    SELECT_RENTAL_PERIOD_FOUR_DAYS = (By.XPATH, '//div[text()="четверо суток"]')

    SCOOTER_COLOR_BLACK = (By.XPATH, '//*[@id="black"]' )
    SCOOTER_COLOR_GREY = (By.XPATH, '//*[@id="grey"]')
    INPUT_COMMENT_FOR_COURIER = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    BUTTON_ORDER_FINAL = (By.XPATH, '//div//button[2][text()="Заказать"]')
    BUTTON_YES_PLACE_ORDER = (By.XPATH, '//button[text()="Да"]')
    TEXT_ORDER_SUBMITTED = (By.XPATH, '//div[text()="Заказ оформлен"]')

    BUTTON_VIEW_STATUS = (By.XPATH, '//button[text()="Посмотреть статус"]')