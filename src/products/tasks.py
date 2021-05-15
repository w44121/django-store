from django.core.mail import send_mail
from app.celery import app
from products.models import Product
from users.models import User

import logging


logger = logging.getLogger()


def test_email_message(user, product, email=None) -> None:
    if not email:
        if not user.email:
            logger.error(f'error to send email to {email} of notification product arrived {product.id} -> no email')
    try:
        send_mail(
            subject='product arrival notification',
            message=f'hi ,{user}, {product} is arrived',
            from_email='django-store@example.com',
            recipient_list=[email],
            fail_silently=False,
        )
    except Exception as e:
        logger.error(f'error to send email to {email} of notification product arrived {product.id} -> {e}')


@app.task
def send_product_arrival_notification(user_id, product_id) -> None:
    user = User.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)
    test_email_message(
        user=user,
        product=product,
    )
