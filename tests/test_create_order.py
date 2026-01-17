from url import url
from data import *
import allure
from ..methods.create_order_methods import CreateOrderMethods

class TestOrder:
    
    @allure.title('Успешное создание заказа с ингредиентами авторизованным пользователем')
    def test_auth_user_create_order_success(self, created_user):
        response = CreateOrderMethods.auth_user_create_order(created_user)

        assert response == 200

            
    @allure.title('Ошибка 400 при создании заказа без ингредиентов авторизованным пользователем')
    def test_auth_user_create_order_no_ingredients(self, created_user):
        response = CreateOrderMethods.auth_user_create_order_no_ingredients(created_user)

        assert response.status_code == 400
        assert response.json()["message"] == no_ingredients

    @allure.title('Ошибка 500 при создании заказа с несуществующим ингредиентом авторизованным пользователем')
    def test_auth_user_create_order_wrong_ingredient(self, created_user):
        response = CreateOrderMethods.auth_user_create_order_wrong_ingredient(created_user)

        assert response.status_code == 500

    @allure.title('Успешное создание заказа с ингредиентами неавторизованным пользователем')
    def test_create_order_with_ingredient(self):
        response = CreateOrderMethods.create_order()

        assert response == 200

    @allure.title('Ошибка 400 при создании заказа без ингредиентов неавторизованным пользователем')
    def test_create_order_no_ingredient(self):
        response = CreateOrderMethods.create_order_no_ingredient()

        assert response.status_code == 400
        assert response.json()["message"] == no_ingredients

    @allure.title('Ошибка 500 при создании заказа с несуществующим ингредиентом неавторизованным пользователем')
    def test_create_order_wrong_ingredient(self):
        response = CreateOrderMethods.create_order_wrong_ingredient()

        assert response == 500