import pytest
import allure
from Sprint_6.main_page import QuestionsAboutImportant, MainPageLocators


class TestQuestions:
    answer_text_lst = ['Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
                       'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
                       'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
                       'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
                       'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
                       'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
                       'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
                       'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
                       ]
    @pytest.mark.parametrize('locator_quest,locator_ans, answer_text',
                            [[MainPageLocators.TEXT_QUESTION_PRICE, MainPageLocators.TEXT_ANSWER_PRICE, answer_text_lst[0]],
                              [MainPageLocators.TEXT_QUESTION_SCOOTERS, MainPageLocators.TEXT_ANSWER_SCOOTERS, answer_text_lst[1]],
                              [MainPageLocators.TEXT_QUESTION_RENT_TIME, MainPageLocators.TEXT_ANSWER_RENT_TIME, answer_text_lst[2]],
                              [MainPageLocators.TEXT_QUESTION_SCOOTER_TODAY, MainPageLocators.TEXT_ANSWER_SCOOTER_TODAY, answer_text_lst[3]],
                              [MainPageLocators.TEXT_QUESTION_PROLONGATION, MainPageLocators.TEXT_ANSWER_PROLONGATION, answer_text_lst[4]],
                              [MainPageLocators.TEXT_QUESTION_CHARGER, MainPageLocators.TEXT_ANSWER_CHARGER, answer_text_lst[5]],
                              [MainPageLocators.TEXT_QUESTION_CANCELLATIONS, MainPageLocators.TEXT_ANSWER_CANCELLATIONS, answer_text_lst[6]],
                              [MainPageLocators.TEXT_QUESTION_FAR_AWAY, MainPageLocators.TEXT_ANSWER_FAR_AWAY,answer_text_lst[7]]
                            ]
                             )

    @allure.title('Проверка открытия текстового поля с ответами под всеми вопросами из раздела "Вопросы о важном"')
    @allure.description('Сравниваем текст ответов на вопросы раздела "Вопросы о важном" с ожидаемыми текстами')
    def test_question(self, driver, locator_quest, locator_ans, answer_text):
        question_page = QuestionsAboutImportant(driver)
        question_page.go_on_page_scooter()
        question_page.click_on_question(locator_quest)
        answer_text_result = QuestionsAboutImportant(driver)
        assert answer_text_result.check_answer_text(locator_ans) == answer_text
