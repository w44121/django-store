from .models import OrderProduct, Order
from products.models import Product


class OrderCreater:
    def __init__(self, cart, user):
        self.cart = cart
        self.order = Order.objects.create(
            user=user,
            total_price=self.cart.get_sum()
        )

    def _get_products_from_cart(self):
        products = Product.objects.filter(id__in=[x[0] for x in self.cart])
        return products

    def create_new(self):
        for product in self._get_products_from_cart():
            quantity = self.cart.cart[str(product.id)]['quantity']
            order_project = OrderProduct.objects.create(
                quantity=quantity,
                product=product,
            )
            self.order.products.add(order_project)
