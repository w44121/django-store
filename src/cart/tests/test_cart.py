import pytest
from cart.cart import Cart
from products.tests.conftest import product, category, producer  # noqa: F401


@pytest.mark.django_db
def test_create_cart(session):
    cart = Cart(session)

    assert cart.cart == {}


@pytest.mark.django_db
def test_add_product_cart(session, product):
    cart = Cart(session)
    cart.append_item(product)

    assert cart.cart.get('1') is not None
    assert len(cart.cart) == 1
    assert cart.cart['1'] == {'quantity': 1, 'product_title': 'i7 7700', 'price': '100500'}

    cart.append_item(product)

    assert cart.cart['1'] == {'quantity': 2, 'product_title': 'i7 7700', 'price': '100500'}


@pytest.mark.django_db
def test_remove_product_cart(cart_with_products, product):
    cart_with_products.remove_item(product)

    assert cart_with_products.cart.get('1') is None
    assert len(cart_with_products.cart) == 1


@pytest.mark.django_db
def test_clear_cart(cart_with_products, product):

    assert len(cart_with_products.cart) == 2

    cart_with_products.clear()

    assert len(cart_with_products.cart) == 0


@pytest.mark.django_db
def test_count_items_cart(cart_with_products):
    assert cart_with_products.get_count() == 3


@pytest.mark.django_db
def test_sum_price_cart(cart_with_products):
    assert cart_with_products.get_sum() == 301500
