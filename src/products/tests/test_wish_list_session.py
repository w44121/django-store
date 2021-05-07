import pytest
from products.controller import WishListSession
from cart.tests.conftest import session  # noqa: F401


@pytest.mark.django_db
def test_wish_list_session_create(session):
    wls = WishListSession(session)

    assert wls is not None
    assert wls.wish_list == {}


@pytest.mark.django_db
def test_wish_list_session_append_item(wish_list_session, product, product2):
    wish_list_session.append_item(product)

    assert product.id == wish_list_session.wish_list[str(product.id)]
    assert len(wish_list_session.wish_list) == 1

    wish_list_session.append_item(product2)

    assert len(wish_list_session.wish_list) == 2


@pytest.mark.django_db
def test_wish_list_session_remove_item(wish_list_session, product, product2):
    wish_list_session.append_item(product)
    wish_list_session.append_item(product2)

    assert len(wish_list_session.wish_list) == 2

    wish_list_session.remove_item(product)

    assert len(wish_list_session.wish_list) == 1
    assert product2.id == wish_list_session.wish_list[str(product2.id)]


@pytest.mark.django_db
def test_wish_list_session_clear(wish_list_session, product, product2):
    wish_list_session.append_item(product)
    wish_list_session.append_item(product2)

    assert len(wish_list_session.wish_list) == 2

    wish_list_session.clear()

    assert wish_list_session.wish_list == {}
