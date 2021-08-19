from django.db import transaction, IntegrityError, DatabaseError
from django.db.transaction import TransactionManagementError
from .models import Wallet, Transaction
from .models import Transaction as Transaction_model
from orders.models import Order
from users.models import User
from decimal import Decimal
import logging

logger = logging.getLogger()


class NotEnoughFundsForTheOperation(Exception):
    pass


def get_wallet(user: User) -> Wallet:
    try:
        wallet = Wallet.objects.get(user=user)
    except Wallet.DoesNotExist:
        logger.info(f'Create new wallet for user {user.id}')
        wallet = Wallet.objects.create(user=user)
        wallet.save()
    return wallet


class WalletController:
    def __init__(self, user: User) -> None:
        self.user = user
        self.wallet = get_wallet(self.user)

    @property
    def balance(self) -> Decimal:
        return self.wallet.balance

    def reduce_balance(self, order: Order) -> None:
        if self.balance - order.total_price > 0:
            with transaction.atomic():
                transaction_instance = Transaction_model(
                    wallet=self.wallet,
                    user=self.user,
                    amount=order.total_price,
                    order=order,
                )
                transaction_instance.save()
                self.wallet.balance -= order.total_price
                self.wallet.save()
        else:
            raise NotEnoughFundsForTheOperation

    def up_balance(self, amount: Decimal) -> None:
        try:
            logger.info(
                f'start make transaction for up wallet balance '
                f'for user {self.user.id} with amount: {amount}'
            )
            with transaction.atomic():
                transaction_instance = Transaction_model(
                    wallet=self.wallet,
                    user=self.user,
                    amount=amount,
                    order=None,
                )
                transaction_instance.save()
                self.wallet.balance += Decimal(str(amount))
                self.wallet.save()
                logger.info(
                    f'successfully transaction {transaction_instance.id}'
                    f'for user {self.user.id} with amount: {amount}'
                )
        except TransactionManagementError:
            logger.error('fail make transaction for up wallet balance')


class OrderPayment:
    def __init__(self, user: User, order: Order):
        self.user = user
        self.order = order
        self.wallet = WalletController(self.user)

    def pay(self) -> None:
        try:
            with transaction.atomic():
                self.wallet.reduce_balance(order=self.order)
                order_products = self.order.products.all()
                for order_product in order_products:
                    order_product.product.amount -= order_product.quantity
                    order_product.product.save()
        except TransactionManagementError:
            logger.error(f'error processing transaction with order {self.order.id}')
