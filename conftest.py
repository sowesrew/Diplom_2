import pytest
import requests
from helpers import DataGeneration
from data import DataUrls


@pytest.fixture(scope='function')
def create_and_delete_user():
    data_payload = DataGeneration.create_new_user_and_return_login_password()
    yield data_payload
    login = requests.post(DataUrls.BASE_URL + DataUrls.LOGIN_USER, data=data_payload)
    id_user = login.json()["accessToken"]
    requests.delete(DataUrls.BASE_URL + DataUrls.EDIT_USER, headers={"Authorization": id_user})


@pytest.fixture(scope='function')
def create_and_delete_edit_user():
    data_payload = DataGeneration.create_new_user_and_return_login_password()
    create = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_USER, data=data_payload)
    id_user = create.json()["accessToken"]
    yield id_user
    requests.delete(DataUrls.BASE_URL + DataUrls.EDIT_USER, headers={"Authorization": id_user})
