from rest_framework import serializers
from .models import (
    Producer,
    Category,
    Product,
    Image,
)


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
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
    image = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']
