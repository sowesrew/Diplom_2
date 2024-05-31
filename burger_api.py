import requests
import allure
from helpers import DataGeneration
from data import DataUrls


class MethodsUser:
# создание юзера
    @staticmethod
    @allure.step("Создание уникального пользователя в системе")
    def create_user(payload):
        response = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_USER, payload)
        return response

    @staticmethod
    @allure.step("Логин пользователя в систему")
    def login_user(payload):
        requests.post(DataUrls.BASE_URL + DataUrls.CREATE_USER, payload)
        response = requests.post(DataUrls.BASE_URL + DataUrls.LOGIN_USER, payload)
        return response