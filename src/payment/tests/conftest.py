from django.contrib.sessions.backends.db import SessionStore
from orders.controller import OrderCreator
from cart.cart import Cart
from products.models import Product, Category, Producer
from users.models import User
import pytest


@pytest.fixture
def user():
    user = User.objects.create_user(
        id=1,
        username='test_user',
        password='test_password',
    )
    return user


@pytest.fixture
def category():
    return Category.objects.create(
        title='cpu',
        description='cpu description',
    )


@pytest.fixture
def producer():
    return Producer.objects.create(
        title='amd',
        description='amd description',
    )


@pytest.fixture
def product(category, producer):
    return Product.objects.create(
        id=1,
        title='i7 7700',
        description='i7 7700 description',
        category=category,
        producer=producer,
        characteristics={
            'cores': 8
        },
        price=300,
        amount=100,
    )


@pytest.fixture
def product2(category, producer):
    return Product.objects.create(
        id=2,
        title='r5 5600',
        description='r5 5600 description',
        category=category,
        producer=producer,
        characteristics={
            'cores': 8
        },
        price=100,
        amount=100,
    )


@pytest.fixture
def cart_with_products(session):
    cart = Cart(session)
    cart.cart['1'] = {'quantity': 1, 'price': '100'}
    cart.cart['2'] = {'quantity': 2, 'price': '200'}
    return cart


@pytest.fixture
def session():
    return SessionStore()


@pytest.fixture
def cart(session):
    return Cart(session)


@pytest.fixture
def order(cart_with_products, user,  product, product2):
    return OrderCreator(cart_with_products, user).create_new()

