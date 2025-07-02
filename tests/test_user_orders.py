import requests
import allure
from tests.data import BASE_URL, MSG_UNAUTHORIZED

@allure.feature("Получение заказов пользователя")
class TestUserOrders:
    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_authorized(self, create_and_delete_user):
        token = create_and_delete_user["accessToken"]
        headers = {"Authorization": token}
        response = requests.get(f"{BASE_URL}/api/orders", headers=headers)
        assert response.status_code == 200
        assert "orders" in response.json()

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_orders_unauthorized(self):
        response = requests.get(f"{BASE_URL}/api/orders")
        assert response.status_code == 401
        assert response.json()["message"] == MSG_UNAUTHORIZED 