import allure
from Sprint_6.logo_scooter_dzen import LogoScooter
from Sprint_6.rent_scooter import RentScooter


class TestLogo:
    @allure.title('Проверка того, что если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    @allure.description('На странице определяем текущий URL и сравниваем его с "https://qa-scooter.praktikum-services.ru/"')
    def test_logo_on_click_scooter(self, driver):
        order = RentScooter(driver)
        order.go_on_page_scooter()
        order.rent_button_top()
        logo = LogoScooter(driver)
        logo.logo_scooter_on_click()
        assert logo.check_home_page_url() == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка того,что если нажать на логотип "Яндекса", в новом окне через редирект откроется главная страница Дзена')
    @allure.description('На странице определяем текущий URL и сравниваем его с "https://dzen.ru/?yredirect=true"')
    def test_logo_on_click_dzen(self, driver):
        page = RentScooter(driver)
        page.go_on_page_scooter()
        logo = LogoScooter(driver)
        logo.logo_dzen_on_click()
        logo.switch_to_dzen_tab()
        logo.wait_for_upload_dzen_page()
        assert logo.check_home_page_url() == 'https://dzen.ru/?yredirect=true'
