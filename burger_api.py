import requests
import allure
from helpers import DataGeneration
from data import DataUrls
from conftest import create_and_delete_user


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
    @allure.step("Попытка создания пользователя без обязательного поля")
    def not_once_required_field():
        data_email = DataGeneration.create_new_user_and_return_login_password()["email"]
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
    @allure.step("Логин пользователя в систему c неверными данными")
    def login_no_such_username_and_password():
        data_payload = DataGeneration.create_new_user_and_return_login_password()
        response = requests.post(DataUrls.BASE_URL + DataUrls.LOGIN_USER, data=data_payload)
        return response

    @staticmethod
    @allure.step("Создание, логин и изменение данных пользователя")
    def create_login_edit_user(data_payload, data_edit):
        requests.post(DataUrls.BASE_URL + DataUrls.CREATE_USER, data=data_payload)
        login = requests.post(DataUrls.BASE_URL + DataUrls.LOGIN_USER, data=data_payload)
        id_user = login.json()["accessToken"]
        response = requests.patch(DataUrls.BASE_URL + DataUrls.LOGIN_USER, data=data_edit, headers={"Authorization": id_user})
        return response

