import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class RentScooterLocators:
    ORDER_BUTTON_TOP = [By.XPATH, "//button[@class='Button_Button__ra12g']"]
    ORDER_BUTTON_DOWN = [By.XPATH, "//div[@class='Home_FinishButton__1_cWm']"]

class RentScooter(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по верхней кнопке "Заказать"')
    def rent_button_top(self):
        self.find_element_rent(RentScooterLocators.ORDER_BUTTON_TOP).click()

    @allure.step('Клик по нижней кнопке "Заказать"')
    def rent_button_down(self):
        element = self.find_element_rent(RentScooterLocators.ORDER_BUTTON_DOWN)
        self.scrolling_to_element(element)
        self.find_element_rent_click(RentScooterLocators.ORDER_BUTTON_DOWN)
