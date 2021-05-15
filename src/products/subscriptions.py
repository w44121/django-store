from products.models import Product, SubscriptionProductArrival
import logging


logger = logging.getLogger()


def subscribe_to_product_arrival_notification(user, product_id: int, email=None) -> None:
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        logger.warning(f'user {user.id} attempting to subscribe to a non-existent product {product_id}')
        raise Product.DoesNotExist

    try:
        SubscriptionProductArrival.objects.get(
            product=product,
            user=user,
        )
        logger.warning(f'user {user.id} has allready subscribed to notification of the arrival product {product_id}')
        return
    except Exception:
        pass

    if not product.is_stock:
        logger.warning(f'user {user.id} attempting to subscribe to a product in stock {product_id}')
        return

    SubscriptionProductArrival.objects.create(
        product=product,
        user=user,
    ).save()
    logger.info(f'user {user.id} has successfully subscribe to notification of the arrival product {product_id}')
