import allure
from burger_api import MethodsUser
from conftest import create_and_delete_user


class TestRegisterNewUser:
    @allure.title("Проверка создания уникального пользователя")
    @allure.description("Создаём пользователя, убеждаемся, что приходит верный код ответа")
    def test_successful_create_user(self, create_and_delete_user):
        user = MethodsUser.create_user(create_and_delete_user)
        assert user.status_code == 200 and '"success":true' in user.text

    @allure.title("Проверка создания пользователя, данные которого уже имеются в системе")
    @allure.description("Создаём пользователя повторно, убеждаемся, что приходит верный код ответа")
    def test_duplicate_create_user(self, create_and_delete_user):
        user = MethodsUser.dublicate_create_user(create_and_delete_user)
        assert user.status_code == 403 and '"message":"User already exists"' in user.text

    @allure.title("Проверка создания пользователя, но одно из обязательных полей не заполнено")
    @allure.description("Создаём пользователя без указания одного из обязательных полей")
    def test_not_once_required_field(self):
        user = MethodsUser.not_once_required_field()
        assert user.status_code == 403 and user.json()['message'] == 'Email, password and name are required fields'
