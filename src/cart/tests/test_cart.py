import pytest
from cart.cart import Cart
from products.tests.conftest import product, category, producer  # noqa: F401


def test_create_cart(session):
    cart = Cart(session)

    assert cart.cart == {}


@pytest.mark.django_db
def test_add_product_in_cart(session, product):
    cart = Cart(session)
    cart.append_item(product)

    assert cart.cart.get('1') is not None
    assert len(cart.cart) == 1
    assert cart.cart['1'] == {'quantity': 1, 'price': '100500'}

    cart.append_item(product)

    assert cart.cart['1'] == {'quantity': 2, 'price': '100500'}


@pytest.mark.django_db
def test_remove_product_from_cart(session, product):
    cart = Cart(session)
    cart.append_item(product)
    cart.remove_item(product)

    assert cart.cart.get('1') is None
    assert len(cart.cart) == 0
