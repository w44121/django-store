from .models import OrderProduct, Order
from products.models import Product


class ProductInCartDoesNotExistInDatabase(Exception):
    pass


class CreateOrderWithEmptyCart(Exception):
    pass


class OrderCreater:
    def __init__(self, cart, user):
        self.cart = cart
        self.order = Order.objects.create(
            user=user,
            total_price=self.cart.get_sum()
        )

    def _check_products(self, products):
        if len(self.cart.cart) != products.count():
            raise ProductInCartDoesNotExistInDatabase
        elif len(self.cart.cart) == 0:
            raise CreateOrderWithEmptyCart
        return True

    def _get_products_from_cart(self) -> list[Product]:
        products = Product.objects.filter(id__in=[x[0] for x in self.cart])
        if self._check_products(products):
            return products

    def create_new(self):
        for product in self._get_products_from_cart():
            quantity = self.cart.cart[str(product.id)]['quantity']
            order_products = OrderProduct.objects.create(
                quantity=quantity,
                product=product,
            )
            self.order.products.add(order_products)
        return self.order
