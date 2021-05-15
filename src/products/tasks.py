from app.celery import app
from products.models import Product
from users.models import User

import logging


logger = logging.getLogger()


def test_mock_message(user, product):
    print(f'hi ,{user}, {product} arrived')


@app.task
def send_product_arrival_notification(user_id, product_id) -> None:
    user = User.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)
    test_mock_message(
        user=user,
        product=product,
    )
