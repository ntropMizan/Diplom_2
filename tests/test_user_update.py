import requests
import pytest
import allure
from tests.data import USER_VALID, MSG_UNAUTHORIZED
from urls import BASE_URL

@allure.feature("Изменение данных пользователя")
class TestUserUpdate:
    @allure.title("Изменение данных пользователя с авторизацией")
    def test_update_user_authorized(self, create_and_delete_user):
        token = create_and_delete_user["accessToken"]
        headers = {"Authorization": token}
        new_data = {"name": "Изменённый Имя"}
        response = requests.patch(f"{BASE_URL}/api/auth/user", headers=headers, json=new_data)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == new_data["name"]

    @allure.title("Изменение данных пользователя без авторизации")
    def test_update_user_unauthorized(self):
        new_data = {"name": "Кто-то"}
        response = requests.patch(f"{BASE_URL}/api/auth/user", json=new_data)
        assert response.status_code == 401
        assert response.json()["message"] == MSG_UNAUTHORIZED 