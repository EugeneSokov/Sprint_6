import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class OrderLocators:
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    FAMILY = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH,"//input[@class='select-search__input']")
    METRO_STATION =(By.CLASS_NAME,'select-search__select')
    TELEPHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, 'Dropdown-arrow')
    RENTAL_PERIOD_LIST = (By.XPATH, "//div[contains(text(),'двое суток')]")
    COLOR_SCOOTER = (By.XPATH, "//input[@id='grey']")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON_CONFIRM = (By.XPATH, "//button[contains(text(),'Да')]")
    ORDER_STATUS_CONFIRM = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")

class ORDER_FORM(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввод данных в форму 1 заказа самоката')
    def input_data_in_form(self, name, surname, address, metro_station, telephone):
        name_field = self.find_element_rent(OrderLocators.NAME)
        name_field.send_keys(name)
        family_field = self.find_element_rent(OrderLocators.FAMILY)
        family_field.send_keys(surname)
        address_field = self.find_element_rent(OrderLocators.ADDRESS)
        address_field.send_keys(address)
        metro_field = self.find_element_rent(OrderLocators.METRO)
        metro_field.send_keys(metro_station)
        metro_field_station = self.find_element_rent_click(OrderLocators.METRO_STATION)
        telephone_field = self.find_element_rent(OrderLocators.TELEPHONE)
        telephone_field.send_keys(telephone)

    @allure.step('Ввод данных в форму 2 заказа самоката(2)')
    def input_data_in_form_time(self, date, comment):
        date_field = self.find_element_rent(OrderLocators.DATE_FIELD)
        date_field.send_keys(date)
        period_field = self.find_element_rent_click(OrderLocators.RENTAL_PERIOD_FIELD)
        period_input = self.find_element_rent_click(OrderLocators.RENTAL_PERIOD_LIST)
        color_scooter = self.find_element_rent_click(OrderLocators.COLOR_SCOOTER)
        comment_field = self.find_element_rent(OrderLocators.COMMENT)
        comment_field.send_keys(comment)

    @allure.step('Клик по кнопке "Заказать"')
    def click_next_button(self):
        return self.find_element_rent_click(OrderLocators.NEXT_BUTTON)

    @allure.step('Клик по кнопке "Да"')
    def click_next_button_confirm(self):
        self.find_element_rent(OrderLocators.ORDER_BUTTON_CONFIRM)
        return self.find_element_rent_click(OrderLocators.ORDER_BUTTON_CONFIRM)

    @allure.step('Текст кнопки подтверждения заказа')
    def confirmation_of_the_order(self):
        return self.ordering_success(OrderLocators.ORDER_STATUS_CONFIRM).text
