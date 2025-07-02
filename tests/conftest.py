import pytest
import requests
import uuid
from tests.data import BASE_URL, USER_VALID

def generate_unique_user():
    unique_email = f"test_user_{uuid.uuid4().hex[:8]}@example.com"
    user = USER_VALID.copy()
    user["email"] = unique_email
    return user

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