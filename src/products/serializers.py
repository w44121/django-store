from rest_framework import serializers
from .models import (
    Producer,
    Category,
    Product,
)


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    producer = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title',
    )
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title',
    )

    class Meta:
        model = Product
        fields = '__all__'


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']
