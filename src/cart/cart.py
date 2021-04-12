from django.conf import settings
from products.models import Product
from decimal import Decimal


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = {}
        self.cart = cart

    def append_item(self, product: Product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': quantity,
                'price': str(product.price)
            }
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove_item(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def clear(self):
        self.cart = {}
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
    
    def get_count(self):
        return sum(x['quantity'] for x in self.cart.values())

    def get_sum(self):
        return sum(Decimal(x['price']) * x['quantity'] for x in self.cart.values())

    def __iter__(self):
        for item in self.cart.items():
            yield item
