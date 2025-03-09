from selenium.webdriver.common.by import By

class HomePageLocators:

    BUTTON_ORDER_BUTTON_OF_THE_PAGE = (By.XPATH, '//div[4]//button[1][text()="Заказать"]')
    TEXT_QUESTION_ABOUT_IMPORTANT = (By.XPATH,'//div[text()="Вопросы о важном"]')

    BUTTON_QUESTION_0  = (By.ID, 'accordion__heading-0')
    TEXT_ANSWER_0 = (By.ID, 'accordion__panel-0')

    BUTTON_QUESTION_1  = (By.ID, 'accordion__heading-1')
    TEXT_ANSWER_1 = (By.ID, 'accordion__panel-1')

    BUTTON_QUESTION_2  = (By.ID, 'accordion__heading-2')
    TEXT_ANSWER_2 = (By.ID, 'accordion__panel-2')

    BUTTON_QUESTION_3  = (By.ID, 'accordion__heading-3')
    TEXT_ANSWER_3 = (By.ID, 'accordion__panel-3')

    BUTTON_QUESTION_4  = (By.ID, 'accordion__heading-4')
    TEXT_ANSWER_4 = (By.ID, 'accordion__panel-4')

    BUTTON_QUESTION_5  = (By.ID, 'accordion__heading-5')
    TEXT_ANSWER_5 = (By.ID, 'accordion__panel-5')

    BUTTON_QUESTION_6  = (By.ID, 'accordion__heading-6')
    TEXT_ANSWER_6 = (By.ID, 'accordion__panel-6')

    BUTTON_QUESTION_7  = (By.ID, 'accordion__heading-7')
    TEXT_ANSWER_7 = (By.ID, 'accordion__panel-7')

