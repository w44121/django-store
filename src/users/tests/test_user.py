import pytest
from users.models import User


@pytest.mark.django_db
def test_user_create():
    user = User.objects.create_user(
        username='testuser',
        password='testpassword',
    )
    assert isinstance(user, User)
    assert user.is_staff is False
