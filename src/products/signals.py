from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product, SubscriptionProductArrival
from .tasks import send_product_arrival_notification
import logging


logger = logging.getLogger()


def is_product_arrived(product: Product) -> bool:
    """
    Use only with pre_save signal!
    """
    product_before_save = Product.objects.get(id=product.id)
    return not product_before_save.is_stock and product.is_stock


@receiver(pre_save, weak=False, sender=Product)
def product_pre_save(sender, instance, *args, **kwargs) -> None:
    if is_product_arrived(instance):
        print('new product')
        for subcribe in SubscriptionProductArrival.objects.filter(product=instance):
            print(subcribe.user.id, instance.id)
            send_product_arrival_notification.apply_async(kwargs={
                'user_id': subcribe.user.id,
                'product_id': instance.id,
            })
