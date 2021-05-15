from django.db import models
from users.models import User
from app.models import TimeStampedModel


class Producer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.title).capitalize()


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.title).capitalize()


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(default='no_image.png')  # default image on back?
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='products')
    characteristics = models.JSONField(default=dict)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    released = models.BooleanField(default=False)
    release_date = models.DateTimeField(auto_now=True)

    @property
    def is_stock(self) -> bool:
        return self.amount > 0

    def __str__(self):
        return f'{self.category} {self.producer} {self.title}'


class FavoriteProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorit_products')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorit_products')

    def __str__(self):
        return f'{self.user}, {self.product}'


class SubscriptionProductArrival(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='subscriptions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')

    def __str__(self):
        return f'{self.user} subscribe to arrival {self.product}'
