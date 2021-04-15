from cart.cart import Cart
from .models import OrderProduct, Order
from products.models import Product


class OrderHandler:
    def __init__(self, request):
        self.request = request
        self.cart = Cart(request)
        self.order = Order.objects.create(
            user=self.request.user,
            total_price=self.cart.get_sum()
        )

    def create(self):
        # Проблема с цекличными запросами
        # Разбить логику на несколько методов или классов
        print('<1>', [x for x in self.cart])

        # Получение кверисета с продуктами(для заказа)
        order_products = [OrderProduct.objects.create(
            # Получение моделей продуктов из корзины
            product=Product.objects.get(id=int(product[0])),
            quantity=product[1]['quantity'],
        ) for product in self.cart]

        print('<2>', order_products)
        self.order.products.add(*order_products)
        print('<3>', self.order)

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
