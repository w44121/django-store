from django.db import models
from app.models import TimeStampedModel
from users.models import User
from products.models import Product


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_pruducts')
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity}: {self.product}'


class Order(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.ManyToManyField(OrderProduct, related_name='orders')
    is_paid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} {self.total_price} {self.is_paid} {self.is_active}'
