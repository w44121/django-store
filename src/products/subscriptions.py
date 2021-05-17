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

    if product.is_stock:
        logger.warning(f'user {user.id} attempting to subscribe to a product in stock {product_id}')
        return

    SubscriptionProductArrival.objects.create(
        product=product,
        user=user,
    ).save()
    logger.info(f'user {user.id} has successfully subscribe to notification of the arrival product {product_id}')


def unsubscribe_from_product_arrival_notification(user, product_id):
    try:
        subscribe = SubscriptionProductArrival.objects.get(
            product__id=product_id,
            user=user,
        )
    except subscribe.DoesNotExist:
        logger.error(f'an error occurred when the user {user.id} tried to unsubscribe from notifications about the arrival of a product {product_id}')
        raise subscribe.DoesNotExist

    subscribe.delete()
    logger.info(f'user {user.id} has successfully unsubscribed from product {product_id} arrival notifications')
