import pytest
import allure
from ..methods.create_user_methods import CreateUserMethods
from ..data import *


class TestCreateCourier:
    @allure.title("Проверка создания пользователя при передачи имени, логина и пароля")
    def test_create_user_success(self):
        response = CreateUserMethods.register_new_user_and_return_login_password()
        assert len(response) == 3

    @allure.title(
        "Проверка возникновения ошибки 403 при попытке создания двух одинаковых пользователей"
    )
    def test_create_two_same_users(self):
        response = CreateUserMethods.register_two_same_users()
        assert response.status_code == 403
        assert response.json()["message"] == user_exists

    @allure.title(
        "Проверка возникновения ошибки 403 при попытке создания пользователя, не заполнив одно обязательное поле Логин"
    )
    def test_missing_login_failed(self):
        response = CreateUserMethods.required_login_is_missing()
        assert response.status_code == 403
        assert response.json()["message"] == not_enough_data

    @allure.title(
        "Проверка возникновения ошибки 403 при попытке создания пользователя, не заполнив одно обязательное поле Пароль"
    )
    def test_missing_password_failed(self):
        response = CreateUserMethods.required_password_is_missing()
        assert response.status_code == 403
        assert response.json()["message"] == not_enough_data

    @allure.title(
        "Проверка возникновения ошибки 403 при попытке создания пользователя, не заполнив одно обязательное поле Имя"
    )
    def test_name_password_failed(self):
        response = CreateUserMethods.required_name_is_missing()
        assert response.status_code == 403
        assert response.json()["message"] == not_enough_data
