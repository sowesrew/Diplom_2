import requests
import allure
from helpers import DataGeneration
from data import DataUrls, DataOrder


class MethodsUser:
    @staticmethod
    @allure.step("Создание уникального пользователя в системе")
    def create_user(data_payload):
        response = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_USER, data=data_payload)
        return response

    @staticmethod
    @allure.step("Создание дубликата пользователя в системе")
    def dublicate_create_user(data_payload):
        requests.post(DataUrls.BASE_URL + DataUrls.CREATE_USER, data=data_payload)
        response = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_USER, data=data_payload)
        return response

    @staticmethod
    @allure.step("Попытка создания пользователя без поля Пароль")
    def not_once_required_field():
        data_email = DataGeneration.generated_user_data_and_return_login_password()["email"]
        data = {
            "email": data_email,
            "password": ""
        }
        response = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_USER, data=data)
        return response

    @staticmethod
    @allure.step("Логин пользователя в систему")
    def login_user(data_payload):
        requests.post(DataUrls.BASE_URL + DataUrls.CREATE_USER, data=data_payload)
        response = requests.post(DataUrls.BASE_URL + DataUrls.LOGIN_USER, data=data_payload)
        return response

    @staticmethod
    @allure.step("Тест на авторизацию с несуществующим в системе данными")
    def login_no_such_username_and_password():
        data_payload = DataGeneration.generated_user_data_and_return_login_password()
        response = requests.post(DataUrls.BASE_URL + DataUrls.LOGIN_USER, data=data_payload)
        return response

    @staticmethod
    @allure.step("Создание, логин и изменение данных пользователя")
    def create_and_edit_user(edit_field, id_user):
        response = requests.patch(DataUrls.BASE_URL + DataUrls.EDIT_USER, headers={"Authorization": id_user}, data=edit_field)
        return response

    @staticmethod
    @allure.step("Попытка изменения данных пользователя без авторизационного токена")
    def create_and_edit_not_token_user(edit_field):
        response = requests.patch(DataUrls.BASE_URL + DataUrls.EDIT_USER, data=edit_field)
        return response


class OrderUser:
    @staticmethod
    @allure.step("Создание заказа с ингредиентами")
    def create_order_with_token(data_payload):
        create = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_USER, data=data_payload)
        id_user = create.json()["accessToken"]
        response = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_ORDER, data=DataOrder.ingredient, headers={"Authorization": id_user})
        return response

    @staticmethod
    @allure.step("Создание заказа с ингредиентами")
    def create_order_without_token():
        response = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_ORDER, data=DataOrder.ingredient)
        return response

    @staticmethod
    @allure.step("Создание заказа без ингредиентов")
    def create_order_without_ingredients():
        response = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_ORDER, data={})
        return response

    @staticmethod
    @allure.step("Создание заказа с некорректным хешем ингредиентов")
    def create_order_with_incorrect_ingredient():
        response = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_ORDER, data=DataOrder.incorrect_burger)
        return response

    @staticmethod
    @allure.step("Получение списка заказов авторизованного пользователя")
    def receive_order_with_token(data_payload):
        create = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_USER, data=data_payload)
        id_user = create.json()["accessToken"]
        response = requests.get(DataUrls.BASE_URL + DataUrls.CREATE_ORDER, headers={"Authorization": id_user})
        return response

    @staticmethod
    @allure.step("Получение списка заказов авторизованного пользователя")
    def receive_order_without_token():
        response = requests.get(DataUrls.BASE_URL + DataUrls.CREATE_ORDER)
        return response
