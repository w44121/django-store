from django.db import models
from users.models import User
from orders.models import Order
from app.models import TimeStampedModel


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.user} {self.balance}'


class Transaction(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='transactions', null=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def to(self):
        if self.order is None:
            return f'order {self.order.id}'
        return f'wallet {self.wallet.id}'

    def __str__(self):
        return f'from user {self.user.id} to {self.to()}: {self.amount}'
