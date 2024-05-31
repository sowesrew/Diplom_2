import random
import string
import json
#from faker import Faker


class DataGeneration:
    @classmethod
    def create_new_user_and_return_login_password(cls):

        def random_email():
            return ''.join(random.choice(string.ascii_letters) for _ in range(10)) + "@ya.ru"

        def generate_random_string(length = 10):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        email = random_email()
        password = generate_random_string()
        name = generate_random_string()

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        # возвращаем список
        return payload
