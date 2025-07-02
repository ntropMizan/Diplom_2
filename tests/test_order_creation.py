import requests
import allure
from tests.data import BASE_URL, ORDER_INGREDIENTS, ORDER_INVALID_INGREDIENTS, MSG_INGREDIENTS_REQUIRED, MSG_UNAUTHORIZED

@allure.feature("Создание заказа")
class TestOrderCreation:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_authorized(self, create_and_delete_user):
        token = create_and_delete_user["accessToken"]
        headers = {"Authorization": token}
        data = {"ingredients": ORDER_INGREDIENTS}
        response = requests.post(f"{BASE_URL}/api/orders", headers=headers, json=data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации и с ингредиентами")
    def test_create_order_unauthorized(self):
        data = {"ingredients": ORDER_INGREDIENTS}
        response = requests.post(f"{BASE_URL}/api/orders", json=data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_no_ingredients(self):
        data = {"ingredients": []}
        response = requests.post(f"{BASE_URL}/api/orders", json=data)
        assert response.status_code == 400
        assert response.json()["message"] == MSG_INGREDIENTS_REQUIRED

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredients(self):
        data = {"ingredients": ORDER_INVALID_INGREDIENTS}
        response = requests.post(f"{BASE_URL}/api/orders", json=data)
        assert response.status_code == 500 or response.status_code == 400 