import allure
from burger_api import OrderUser
from conftest import create_and_delete_user


class TestReceiveOrder:
    @allure.title("Получение заказов от авторизованного пользователя")
    @allure.description("Получаем заказы с авторизационным токеном")
    def test_receive_order_with_token(self, create_and_delete_user):
        order = OrderUser.receive_order_with_token(create_and_delete_user)
        assert order.status_code == 200 and '"success":true' in order.text

    @allure.title("Получение заказов от неавторизованного пользователя")
    @allure.description("Получаем заказы без авторизационного токена")
    def test_receive_order_without_token(self):
        order = OrderUser.receive_order_without_token()
        assert order.status_code == 401 and order.json()['message'] == 'You should be authorised'


