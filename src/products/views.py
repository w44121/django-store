from rest_framework import generics
from .models import (
    Producer,
    Category,
    Product,
)
from .serializers import (
    ProducerSerializer,
    CategorySerializer,
    ProductSerializer,
)


class ProdcutList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
