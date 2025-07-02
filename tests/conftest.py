import pytest
import requests
import uuid
from helpers import generate_unique_user
from urls import BASE_URL

@pytest.fixture
def create_and_delete_user():
    user_data = generate_unique_user()
    # Создание пользователя
    response = requests.post(f"{BASE_URL}/api/auth/register", json=user_data)
    result = response.json()
    # Добавляем email для последующего логина
    result["email"] = user_data["email"]
    yield result
    # Удаление пользователя после теста, если был создан
    if response.status_code == 200 and 'accessToken' in result:
        token = result['accessToken']
        headers = {"Authorization": token}
        requests.delete(f"{BASE_URL}/api/auth/user", headers=headers) 