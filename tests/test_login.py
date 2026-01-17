import allure 
import requests
from url import url
from data import *

class TestLogin:
    
    @allure.title('Проверка успешной авторизации при введении существующего логина и пароля')
    def test_user_login_with_fixture(self, created_user):
        login, password, first_name = created_user
    
        auth_payload = {"email": login, "password": password, "name": first_name}
        response = requests.post(url.LOGIN_ENDPOINT, data=auth_payload)
    
        assert response.status_code == 200
        response_json = response.json()
        assert "accessToken" in response_json

    @allure.title('Проверка ошибки авторизации 401 при вводе неправильного пароля')
    def test_login_with_wrong_password_failed(self, created_user):
        login, password, first_name = created_user
    
        auth_payload = {"email": login, "password": f'{password}1', "name": first_name}
        response = requests.post(url.LOGIN_ENDPOINT, data=auth_payload)
    
        assert response.status_code == 401
        assert response.json()["message"] == failed_login

    @allure.title('Проверка ошибки авторизации 401 при вводе неправильного логина')
    def test_login_with_wrong_login_failed(self, created_user):
        login, password, first_name = created_user
    
        auth_payload = {"email": f'{login}1', "password": password, "name": first_name}
        response = requests.post(url.LOGIN_ENDPOINT, data=auth_payload)
    
        assert response.status_code == 401
        assert response.json()["message"] == failed_login