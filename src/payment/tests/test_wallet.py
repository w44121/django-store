from payment.models import Wallet
from products.models import Product
from decimal import Decimal
from payment.controller import (
    get_wallet,
    WalletController,
    OrderPayment,
)
import pytest


@pytest.mark.django_db
def test_get_wallet_new_create(user):
    wallet = get_wallet(user)

    assert wallet.balance == 0
    assert wallet.user == user


@pytest.fixture
def wallet(user):
    return Wallet.objects.create(user=user, balance=1000.00)


@pytest.mark.django_db
def test_get_wallet_allready_exist(user, wallet):
    wallet = get_wallet(user)

    assert wallet.balance == 1000
    assert wallet.user == user


@pytest.mark.django_db
def test_wallet_up_balance(user, wallet):
    assert wallet.balance == Decimal('1000.00')

    wallet = WalletController(user)
    wallet.up_balance(500.80)

    assert wallet.balance == Decimal('1500.80')

    wallet = Wallet.objects.get(user=user)

    assert wallet.balance == Decimal('1500.80')


@pytest.mark.django_db
def test_order_payment(user, order, wallet, product, product2):
    assert order.total_price == 500
    assert wallet.balance == Decimal('1000.00')

    order_pay = OrderPayment(user=user, order=order)

    order_pay.pay()

    wallet = Wallet.objects.get(user=user)

    assert wallet.balance == Decimal('500.00')

    product = Product.objects.get(id=1)
    product2 = Product.objects.get(id=2)

    assert product.amount == 99
    assert product2.amount == 98
