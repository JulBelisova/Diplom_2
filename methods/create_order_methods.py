import requests
import random
import string
import allure
from ..url import url

class CreateOrderMethods:
    
    @staticmethod
    @allure.step('Авторизация пользователем и создание заказа c добавлением двух ингредиентов')
    def auth_user_create_order(created_user):
        
        login, password, first_name = created_user
    
        auth_payload = {"email": login, "password": password, "name": first_name}
        response = requests.post(url.LOGIN_ENDPOINT, data=auth_payload)
        

        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
        
        if response.status_code == 200:
            response2 = requests.post(url.ORDER_ENDPOINT, json = payload)

        return response2.status_code
    
    @staticmethod
    @allure.step('Авторизация пользователем и создание заказа без ингредиентов')
    def auth_user_create_order_no_ingredients(created_user):
        
        login, password, first_name = created_user
    
        auth_payload = {"email": login, "password": password, "name": first_name}
        response = requests.post(url.LOGIN_ENDPOINT, data=auth_payload)
        

        payload = {
            "ingredients": []
        }
        
        if response.status_code == 200:
            response2 = requests.post(url.ORDER_ENDPOINT, json = payload)

        return response2
    
    @staticmethod
    @allure.step('Авторизация пользователем и создание заказа c несуществуещем id ингредиента')
    def auth_user_create_order_wrong_ingredient(created_user):
        
        login, password, first_name = created_user
    
        auth_payload = {"email": login, "password": password, "name": first_name}
        response = requests.post(url.LOGIN_ENDPOINT, data=auth_payload)
        

        payload = {
            "ingredients": ["invalid_hash_123"]
        }
        
        if response.status_code == 200:
            response2 = requests.post(url.ORDER_ENDPOINT, json = payload)

        return response2
    
    @staticmethod
    @allure.step('Создание заказа c добавлением двух ингредиентов')
    def create_order():

        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
        
        response = requests.post(url.ORDER_ENDPOINT, json = payload)

        return response.status_code
    
    @staticmethod
    @allure.step('Создание заказа без ингредиентов')
    def create_order_no_ingredient():

        payload = {
            "ingredients": []
        }
        
        response = requests.post(url.ORDER_ENDPOINT, json = payload)

        return response
    
    @staticmethod
    @allure.step('Создание заказа c несуществуещем id ингредиента')
    def create_order_wrong_ingredient():

        payload = {
            "ingredients": ["invalid_hash_123"]
        }
        
        response = requests.post(url.ORDER_ENDPOINT, json = payload)

        return response.status_code