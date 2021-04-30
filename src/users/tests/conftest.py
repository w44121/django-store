import pytest
from users.models import User


@pytest.fixture
def user():
    user = User.objects.create_user(
        id=1,
        username='test_user',
        password='test_password',
    )
    return user
