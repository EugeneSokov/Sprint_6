import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class MainPageLocators:
    QUESTION_FIELD = [By.XPATH,"//div[contains(text(),'Вопросы о важном')]"]
    TEXT_QUESTION_PRICE = (By.ID, 'accordion__heading-0')
    TEXT_QUESTION_SCOOTERS = (By.ID, 'accordion__heading-1')
    TEXT_QUESTION_RENT_TIME = (By.ID, 'accordion__heading-2')
    TEXT_QUESTION_SCOOTER_TODAY = (By.ID, 'accordion__heading-3')
    TEXT_QUESTION_PROLONGATION = (By.ID, 'accordion__heading-4')
    TEXT_QUESTION_CHARGER = (By.ID, 'accordion__heading-5')
    TEXT_QUESTION_CANCELLATIONS = (By.ID, 'accordion__heading-6')
    TEXT_QUESTION_FAR_AWAY = (By.ID, 'accordion__heading-7')
    TEXT_ANSWER_PRICE = (By.XPATH,"//div[@id='accordion__panel-0']/p")
    TEXT_ANSWER_SCOOTERS = (By.XPATH,"//div[@id='accordion__panel-1']/p")
    TEXT_ANSWER_RENT_TIME = (By.XPATH,"//div[@id='accordion__panel-2']/p")
    TEXT_ANSWER_SCOOTER_TODAY = (By.XPATH,"//div[@id='accordion__panel-3']/p")
    TEXT_ANSWER_PROLONGATION = (By.XPATH,"//div[@id='accordion__panel-4']/p")
    TEXT_ANSWER_CHARGER = (By.XPATH,"//div[@id='accordion__panel-5']/p")
    TEXT_ANSWER_CANCELLATIONS = (By.XPATH,"//div[@id='accordion__panel-6']/p")
    TEXT_ANSWER_FAR_AWAY = (By.XPATH,"//div[@id='accordion__panel-7']/p")

class QuestionsAboutImportant(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик на вопрос из раздела "Вопросы о важном')
    def click_on_question(self, locator_quest):
        element = self.find_element_rent(locator_quest)
        self.scrolling_to_element(element)
        self.find_element_rent(locator_quest)
        self.find_element_rent_click(locator_quest)

    @allure.step('Получение текста ответа на вопрос из "Вопросы о важном"')
    def check_answer_text(self, locator_ans):
        answer_field = self.find_element_rent(locator_ans).text
        return answer_field

