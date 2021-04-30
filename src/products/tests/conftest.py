import pytest
from products.models import (
    Product,
    Producer,
    Category,
)


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
        price=100500,
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
        price=100500,
        amount=100,
    )
