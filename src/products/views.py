from rest_framework import generics
from rest_framework.response import Response
from rest_framework import views, status
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
from .controller import WishListSession


class ProdcutList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProducerList(generics.ListAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class WishListView(views.APIView):
    def get(self, request):
        wls = WishListSession(request.session)
        products = Product.objects.filter(id__in=[id for id in wls])
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        WishListSession(request.session).clear()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WishListDetailView(views.APIView):
    def post(self, request, product_id):
        wls = WishListSession(request.session)
        product = Product.objects.get(pk=product_id)
        wls.append_item(product)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, product_id):
        wls = WishListSession(request.session)
        product = Product.objects.get(pk=product_id)
        wls.remove_item(product)
        return Response(status=status.HTTP_204_NO_CONTENT)
