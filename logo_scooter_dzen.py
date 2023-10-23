import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class LogoLocators:
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    LOGO_DZEN = (By.XPATH, "//img[@alt='Yandex']")
    HEADER_DZEN = (By.ID, 'dzen-header')

class LogoScooter(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке логотипа «Самоката»')
    def logo_scooter_on_click(self):
        self.find_element_rent(LogoLocators.LOGO_SCOOTER).click()

    @allure.step('Клик по кнопке логотипа «Яндекс»')
    def logo_dzen_on_click(self):
        self.find_element_rent_click(LogoLocators.LOGO_DZEN)

    @allure.step('Переход на страницу Яндекс.Дзен')
    def switch_to_dzen_tab(self):
        self.go_on_page_dzen()

    @allure.step('Получение URL-адреса страницы')
    def check_home_page_url(self):
        return self.get_page_url()

    @allure.step('Ожидание загрузки страницы Яндекс.Дзен')
    def wait_for_upload_dzen_page(self):
        self.waiting_dzen_page(LogoLocators.HEADER_DZEN)
