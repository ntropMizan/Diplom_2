import requests
import allure
from tests.data import BASE_URL, USER_VALID, MSG_LOGIN_INVALID

@allure.feature("Логин пользователя")
class TestUserLogin:
    @allure.title("Логин под существующим пользователем")
    def test_login_valid_user(self, create_and_delete_user):
        login_data = {
            "email": create_and_delete_user["email"],
            "password": USER_VALID["password"]
        }
        response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
        assert response.status_code == 200
        assert "accessToken" in response.json()

    @allure.title("Логин с неверным логином и паролем")
    def test_login_invalid_user(self):
        login_data = {
            "email": "wrong@example.com",
            "password": "wrongpass"
        }
        response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
        assert response.status_code == 401
        assert response.json()["message"] == MSG_LOGIN_INVALID 