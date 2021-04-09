from django.db import models


class Producer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.title).capitalize()


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.title).capitalize()


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='products')
    characteristics = models.JSONField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.category} {self.producer} {self.title}'
