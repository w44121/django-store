from rest_framework import serializers
from .models import Order, OrderProduct
from products.serializers import ProductOrderSerializer


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductOrderSerializer(read_only=True)

    class Meta:
        model = OrderProduct
        exclude = ['id']


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = '__all__'
