import requests
import allure
from tests.data import USER_VALID, USER_INVALID, USER_ALREADY_EXISTS_EMAIL, MSG_USER_EXISTS, MSG_MISSING_FIELD
from helpers import generate_unique_user
from urls import BASE_URL

@allure.feature("Регистрация пользователя")
class TestUserRegistration:
    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        user_data = generate_unique_user()
        response = requests.post(f"{BASE_URL}/api/auth/register", json=user_data)
        assert response.status_code == 200
        result = response.json()
        assert 'accessToken' in result
        # Удаление пользователя после теста
        if 'accessToken' in result:
            token = result['accessToken']
            headers = {"Authorization": token}
            requests.delete(f"{BASE_URL}/api/auth/user", headers=headers)

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self):
        user = USER_VALID.copy()
        user["email"] = USER_ALREADY_EXISTS_EMAIL
        # Гарантируем, что пользователь уже есть
        requests.post(f"{BASE_URL}/api/auth/register", json=user)
        # Пробуем зарегистрировать повторно
        response = requests.post(f"{BASE_URL}/api/auth/register", json=user)
        assert response.status_code == 403
        body = response.json()
        assert body["success"] is False
        assert body["message"] == MSG_USER_EXISTS

    @allure.title("Создание пользователя без обязательного поля")
    def test_create_user_missing_field(self):
        response = requests.post(f"{BASE_URL}/api/auth/register", json=USER_INVALID)
        assert response.status_code == 403
        assert response.json()["message"] == MSG_MISSING_FIELD 