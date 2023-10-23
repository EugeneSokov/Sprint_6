import pytest
import allure
from Sprint_6.rent_scooter import RentScooter
from Sprint_6.order_page import ORDER_FORM


class TestRentScooter():
    @pytest.mark.parametrize('name,surname,address,metro_station,telephone,date,text',
                             [['Олег', 'Иванов', 'улица Мира,1','Царицыно','+78953578233', '12.12.2023', 'Нет'],
                               ['Игорь','Прокофьев','проспект Просвещения,5','ВДНХ', '+45762345798','27.11.2024','Везите скорее уже']
                             ]
                             )
    @allure.title('Проверка полного флоу позитивного сценария заказа самоката с двумя наборами данных по нажатию на Верхюю кнопку "Заказать"')
    @allure.description('Сравниваем текст кнопки подтверждающего сообщения с "Посмотреть статус"')
    def test_rent_scooter_by_top_button(self, driver, name, surname, address, metro_station, telephone, date, text):
      order = RentScooter(driver)
      order.go_on_page_scooter()
      order.rent_button_top()
      rent_form = ORDER_FORM(driver)
      rent_form.input_data_in_form(name,surname,address,metro_station,telephone)
      rent_form.click_next_button()
      rent_form.input_data_in_form_time(date, text)
      rent_form.click_next_button()
      rent_form.click_next_button_confirm()
      assert rent_form.confirmation_of_the_order() == 'Посмотреть статус'

    @pytest.mark.parametrize('name,surname,address,metro_station,telephone,date,text',
                             [['Павел', 'Кузнецов', 'переулок Независимости,1', 'Белорусская>','+256767492700', '15.08.2024', 'Пустой текст'],
                               ['Кузьма','Варфаламеев','площадь Дворцовая,3', 'Университет','+84261420023','31.12.2023','Ничего не напишу']
                             ]
                             )

    @allure.title('Проверка полного флоу позитивного сценария заказа самоката с двумя наборами данных по нажатию на Нижнюю кнопку "Заказать"')
    @allure.description('Сравниваем текст кнопки подтверждающего сообщения с "Посмотреть статус"')
    def test_rent_scooter_by_down_button(self, driver, name, surname, address, metro_station, telephone, date, text):
      order = RentScooter(driver)
      order.go_on_page_scooter()
      order.rent_button_down()
      rent_form = ORDER_FORM(driver)
      rent_form.input_data_in_form(name,surname,address,metro_station,telephone)
      rent_form.click_next_button()
      rent_form.input_data_in_form_time(date, text)
      rent_form.click_next_button()
      rent_form.click_next_button_confirm()
      assert rent_form.confirmation_of_the_order() == 'Посмотреть статус'
