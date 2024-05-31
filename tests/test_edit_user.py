import allure
import pytest
from burger_api import MethodsUser
from conftest import create_and_delete_user


class TestEditUser:
    @allure.title('Проверка редактирования данных пользователя')
    @allure.description('Проверка успешного редактирования всех полей для пользователя')
    @pytest.mark.parametrize(
        'edit_field',
        [
            ['Svetlana'],
            ['1231jhjrwh@ya.ru'],
            ['4rwerwret4']
        ]
    )
    #def test_success_edit_user(self, edit_field, create_and_delete_user):

