from rest_framework.response import Response
from rest_framework import views
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from .order_creater import OrderCreater
from cart.cart import Cart


class OrderView(views.APIView):
    def get(self, request):
        orders = Order.objects.filter(user=request.user, is_deleted=False)
        serializer = OrderSerializer(orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        cart = Cart(request)
        order = OrderCreater(user=user, cart=cart).create_new()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request):
        orders = Order.objects.filter(user=request.user)
        for order in orders:
            order.is_deleted = True
            order.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderDetailView(views.APIView):
    def get(self, request, order_id):
        order = Order.objects.get(pk=order_id, is_deleted=False)
        serializer = OrderSerializer(data=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, order_id):
        Order.objects.get(pk=order_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
