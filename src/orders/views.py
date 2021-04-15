from rest_framework.response import Response
from rest_framework import views
from .models import Order
from .serializers import OrderSerializer
from .order_handler import OrderHandler


class OrderView(views.APIView):
    def get(self, request):
        orders = Order.objects.filter(user=request.user, is_deleted=False)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        order = OrderHandler(request).create_new()
        return Response(order)

    def delete(self, request):
        orders = Order.objects.filter(user=request.user)
        for order in orders:
            order.is_deleted = True
            order.save()
        return Response()


class OrderDetailView(views.APIView):
    def get(self, request, order_id):
        order = Order.objects.get(pk=order_id, is_deleted=False)
        serializer = OrderSerializer(data=order)
        return Response(data=serializer.data)

    def delete(self, request, order_id):
        Order.objects.get(pk=order_id).delete()
        return Response()
