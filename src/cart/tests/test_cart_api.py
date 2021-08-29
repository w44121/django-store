import pytest
from rest_framework.test import RequestsClient


def test_get_cart():
    client = RequestsClient()
    response = client.get('http://django-store/api/cart/')
    response_data = response.json()

    assert response.status_code == 200
    assert response_data['cart'] == {}
    assert response_data['total quantity'] == 0
    assert response_data['total sum'] == 0
