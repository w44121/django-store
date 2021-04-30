import pytest
from orders.order_creater import OrderCreater, ProductInCartDoesNotExistInDatabase
from cart.tests.conftest import cart_with_products, session  # noqa: F401
from products.tests.conftest import product, product2, category, producer  # noqa: F401
from users.tests.conftest import user  # noqa: F401


@pytest.mark.django_db
def test_order_creater(cart_with_products, user, product, product2):
    order = OrderCreater(cart=cart_with_products, user=user).create_new()

    assert order.user.id == 1
    assert order.user.username == 'test_user'

    assert order.is_active is False
    assert order.is_deleted is False
    assert order.is_paid is False

    assert order.total_price == 301500


@pytest.mark.django_db
def test_order_creater_ProductInCartDoesNotExistInDatabase(cart_with_products, user):
    with pytest.raises(ProductInCartDoesNotExistInDatabase):
        order = OrderCreater(cart=cart_with_products, user=user)
        order.create_new()
