from django.contrib.sessions.backends.db import SessionStore
import pytest


@pytest.fixture
def session():
    return SessionStore()
