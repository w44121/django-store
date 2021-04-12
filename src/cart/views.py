from rest_framework.response import Response
from rest_framework import views
from .cart import Cart
from products.models import Product


class CartView(views.APIView):
    def get(self, request):
        cart = Cart(request)
        data = {
            'cart': cart.cart,
            'total quantity': cart.get_count(),
            'total sum': cart.get_sum(),
       }
        return Response(data)

    def delete(self, request):
        cart = Cart(request)
        cart.clear()
        return Response(cart.cart)


class CartDetailView(views.APIView):
    def post(self, request, product_id):
        cart = Cart(request)
        product = Product.objects.get(pk=product_id)
        cart.append_item(product)
        return Response()

    def delete(self, request, product_id):
        cart = Cart(request)
        product = Product.objects.get(pk=product_id)
        cart.remove_item(product)
        return Response(cart.cart)
