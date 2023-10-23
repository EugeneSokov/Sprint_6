import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = ('https://qa-scooter.praktikum-services.ru/')

    @allure.step('Открываем страницу Яндекс.Самокат')
    def go_on_page_scooter(self):
        return self.driver.get(self.base_url)

    @allure.step('Переход на страницу Яндекс.Дзен')
    def go_on_page_dzen(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Поиск элемента на странице с задержкой=11')
    def find_element_rent(self,locator, time=11):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator), message=f'Not found{locator}')

    @allure.step('Поиск элемента на странице и клик по нему')
    def find_element_rent_click(self, locator):
        self.driver.find_element(*locator).click()
    @allure.step('Поиск элемента на форме для заказа с задержкой=2')
    def ordering_success(self,locator, time=2):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Поиск элемента на странице Яндекс.Дзен с задержкой=12')
    def waiting_dzen_page(self, locator, time=12):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator), message=f'Not found{locator}')

    @allure.step('Возвращение текущего URL-адреса')
    def get_page_url(self):
        return self.driver.current_url

    @allure.step('Скроллинг до элемента на странице')
    def scrolling_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
