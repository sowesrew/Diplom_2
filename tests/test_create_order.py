import allure
from burger_api import OrderUser
from conftest import create_and_delete_user


class TestCreateOrder:
    @allure.title("Проверка создания заказа с авторизацией")
    @allure.description("Проверяется создание заказа с ингредиентами авторизованным пользователем")
    def test_success_create_order_with_token(self, create_and_delete_user):
        order = OrderUser.create_order_with_token(create_and_delete_user)
        assert order.status_code == 200 and order.json()['order']['number'] != 0

    @allure.title("Проверка создания заказа без авторизации")
    @allure.description("Проверяется создание заказа с ингредиентами неавторизованным пользователем")
    def test_success_create_order_without_token(self):
        order = OrderUser.create_order_without_token()
        assert order.status_code == 200 and order.json()['order']['number'] != 0

    @allure.title("Проверка создания заказа без ингредиента")
    @allure.description("Проверяется создание заказа без тела запроса")
    def test_bad_create_order_without_ingredients(self):
        order = OrderUser.create_order_without_ingredients()
        assert order.status_code == 400 and order.json()['message'] == 'Ingredient ids must be provided'

    @allure.title("Проверка создания заказа с некорректными данными")
    @allure.description("Проверяется создание заказа с некорректными данными ингредиентов")
    def test_bad_create_order_with_incorrect_data(self):
        order = OrderUser.create_order_with_incorrect_ingredient()
        assert order.status_code == 500 and 'Internal Server Error' in order.text

