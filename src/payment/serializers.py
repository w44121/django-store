from rest_framework import serializers
from .models import Wallet, Transaction


class WalletSerializer(serializers.ModelSerializer):
    balance = serializers.CharField(read_only=True)

    class Meta:
        model = Wallet
        fields = 'balance'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = '__all__'
