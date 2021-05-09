from rest_framework import generics
from rest_framework.response import Response
from rest_framework import views, status

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

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
from .controller import get_wish_list


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'producer',]
    search_fields = ['title',]
    ordering_fields = ['price']


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProducerList(generics.ListAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class WishListView(views.APIView):
    def get(self, request):
        wish_list = get_wish_list(request)
        products = wish_list.get_products()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        get_wish_list(request).clear()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WishListDetailView(views.APIView):
    def post(self, request, product_id):
        wish_list = get_wish_list(request)
        product = Product.objects.get(pk=product_id)
        wish_list.append_item(product)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, product_id):
        wish_list = get_wish_list(request)
        product = Product.objects.get(pk=product_id)
        wish_list.remove_item(product)
        return Response(status=status.HTTP_204_NO_CONTENT)
