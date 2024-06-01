import allure
import pytest
from burger_api import MethodsUser
from conftest import create_and_delete_edit_user
from helpers import DataUpdateUser


class TestEditUser:
    @allure.title('Проверка редактирования данных пользователя')
    @allure.description('Проверка успешного редактирования всех полей для пользователя')
    @pytest.mark.parametrize(
        'edit_field',
        [
            {"name": "Svetlana"},
            {"email": DataUpdateUser.generation_email()},
            {"password": "4rwerwret4"}
        ]
    )
    def test_success_edit_user(self, edit_field, create_and_delete_edit_user):
        user = MethodsUser.create_and_edit_user(edit_field, create_and_delete_edit_user)
        assert user.status_code == 200 and '"success":true' in user.text


    @allure.title('Проверка редактирования данных пользователя без авторизации')
    @allure.description('Проверка редактирования данных пользователя без авторизационного токена')
    def test_not_token_edit_user(self):
        user = MethodsUser.create_and_edit_not_token_user(edit_field={"name": "Svetlana"})
        assert user.status_code == 401 and user.json()['message'] == 'You should be authorised'