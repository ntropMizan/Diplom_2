# Константы и тестовые данные для API-тестов

# Примеры тестовых данных для пользователей
USER_VALID = {
    "email": "test_user@example.com",
    "password": "123456",
    "name": "Тестовый Пользователь"
}

USER_INVALID = {
    "email": "",
    "password": "123456",
    "name": "Тестовый Пользователь"
}

USER_ALREADY_EXISTS_EMAIL = "already_exists_test@example.com"

# Примеры сообщений API
MSG_USER_EXISTS = "User already exists"
MSG_MISSING_FIELD = "Email, password and name are required fields"
MSG_UNAUTHORIZED = "You should be authorised"
MSG_LOGIN_INVALID = "email or password are incorrect"

# Примеры тестовых данных для заказов (валидные id из /api/ingredients)
ORDER_INGREDIENTS = [
    "61c0c5a71d1f82001bdaaa6d",  # Флюоресцентная булка R2-D3
    "61c0c5a71d1f82001bdaaa6f"   # Мясо бессмертных моллюсков Protostomia
]
ORDER_INVALID_INGREDIENTS = ["invalid_hash"]

# Ожидаемые сообщения
MSG_INGREDIENTS_REQUIRED = "Ingredient ids must be provided" 