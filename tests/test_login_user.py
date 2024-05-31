import allure
from burger_api import MethodsUser
from conftest import create_and_delete_user


class TestLoginNewUser:
    @allure.title("Проверка логина пользователя")
    @allure.description("Создаём пользователя, логинимся и убеждаемся, что приходит верный код ответа")
    def test_login_user(self, create_and_delete_user):
        user = MethodsUser.login_user(create_and_delete_user)
        assert user.status_code == 200 and '"success":true' in user.text

    @allure.title("Проверка логина пользователя с некорректными данными")
    @allure.description("Проверяем логин пользователя, если данные входа некорректны")
    def test_login_user(self):
        user = MethodsUser.login_no_such_username_and_password()
        assert user.status_code == 401 and user.json()['message'] == 'email or password are incorrect'
