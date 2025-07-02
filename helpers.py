import uuid
from tests.data import USER_VALID

def generate_unique_user():
    unique_email = f"test_user_{uuid.uuid4().hex[:8]}@example.com"
    user = USER_VALID.copy()
    user["email"] = unique_email
    return user 