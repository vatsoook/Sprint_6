from selenium.webdriver.common.by import By

class BasePageLocators:

    BUTTON_ORDER_TOP_OF_THE_PAGE = (By.XPATH, '//*[@id="root"]//button[text()="Заказать"]')
    BUTTON_LINK_SCOOTER = (By.CSS_SELECTOR, '.Header_LogoScooter__3lsAR')
    BUTTON_LINK_YANDEX = (By.CSS_SELECTOR, '.Header_LogoYandex__3TSOI')