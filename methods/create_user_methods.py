import requests
import random
import string
import allure
from ..url import url


class CreateUserMethods:
    @staticmethod
    @allure.step('Создание рандомных логина, пароля и имени для создания пользователя')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    
    @staticmethod
    @allure.step('Отправка запроса на регистрацию пользователя с указанием всех данных Логина, Пароля и имени')
    def register_new_user_and_return_login_password():
        login_pass = []

        login = CreateUserMethods.generate_random_string(10)
        password = CreateUserMethods.generate_random_string(10)
        first_name = CreateUserMethods.generate_random_string(10)

        payload = {
            "email": f"{login}@test.com",
            "password": password,
            "name": first_name
        }

        response = requests.post(url.CREATE_USER_ENDPOINT, json=payload)

        if response.status_code == 200:
            login_pass.append(f"{login}@test.com")
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass


    @staticmethod
    @allure.step('Отправка двух одинаковых запроса на регистрацию пользователя с идентичными входными данными')
    def register_two_same_users():

        login = CreateUserMethods.generate_random_string(10)
        password = CreateUserMethods.generate_random_string(10)
        first_name = CreateUserMethods.generate_random_string(10)

        payload = {
            "email": f"{login}@test.com",
            "password": password,
            "name": first_name
        }

        response = requests.post(url.CREATE_USER_ENDPOINT, json=payload)

        if response.status_code == 200:
            return requests.post(url.CREATE_USER_ENDPOINT, json=payload)
        
    @staticmethod
    @allure.step('Отправка запроса на регистрацию пользователя без указания обязательного поля Логин')
    def required_login_is_missing():

        password = CreateUserMethods.generate_random_string(10)
        first_name = CreateUserMethods.generate_random_string(10)

        payload = {
            "password": password,
            "name": first_name
        }

        response = requests.post(url.CREATE_USER_ENDPOINT, json=payload)

        return response
    
    @staticmethod
    @allure.step('Отправка запроса на регистрацию пользователя без указания обязательного поля Пароль')
    def required_password_is_missing():

        login = CreateUserMethods.generate_random_string(10)
        first_name = CreateUserMethods.generate_random_string(10)

        payload = {
            "email": f"{login}@test.com",
            "name": first_name
        }

        response = requests.post(url.CREATE_USER_ENDPOINT, json=payload)

        return response
    
    @staticmethod
    @allure.step('Отправка запроса на регистрацию пользователя без указания обязательного поля Имя')
    def required_name_is_missing():

        login = CreateUserMethods.generate_random_string(10)
        password = CreateUserMethods.generate_random_string(10)

        payload = {
            "email": f"{login}@test.com",
            "password": password
        }

        response = requests.post(url.CREATE_USER_ENDPOINT, json=payload)

        return response