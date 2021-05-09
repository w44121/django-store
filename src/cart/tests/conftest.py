from django.contrib.sessions.backends.db import SessionStore
import pytest
from cart.cart import Cart
from products.tests.conftest import product, category, producer  # noqa: F401


@pytest.fixture
def cart_with_products(session):
    cart = Cart(session)
    cart.cart['1'] = {'quantity': 1, 'price': '100500'}
    cart.cart['2'] = {'quantity': 2, 'price': '100500'}
    return cart


@pytest.fixture
def session():
    return SessionStore()


@pytest.fixture
def cart(session):
    return Cart(session)
