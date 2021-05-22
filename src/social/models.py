from django.db import models
from app.models import TimeStampedModel
from users.models import User
from products.models import Product


class Review(TimeStampedModel):
    advantages = models.TextField(blank=True, null=True)
    minuses = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    rating = models.FloatField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} {self.product}'
