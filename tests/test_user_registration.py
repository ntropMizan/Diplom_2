import requests
import allure
from tests.data import BASE_URL, USER_VALID, USER_INVALID, USER_ALREADY_EXISTS_EMAIL, MSG_USER_EXISTS, MSG_MISSING_FIELD

@allure.feature("Регистрация пользователя")
class TestUserRegistration:
    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, create_and_delete_user):
        assert 'accessToken' in create_and_delete_user

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