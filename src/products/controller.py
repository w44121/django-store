from abc import ABC, abstractmethod
from django.conf import settings
from .models import FavoriteProduct, Product


class WishList(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def append_item(self):
        pass

    @abstractmethod
    def remove_item(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def get_products(self):
        pass


class WishListDataBase(WishList):
    """
    For auth users.
    """
    def __init__(self, user):
        self.user = user

    def append_item(self, product) -> None:
        if not FavoriteProduct.objects.filter(user=self.user).filter(product__id=product.id).count():
            FavoriteProduct.objects.create(
                product=product,
                user=self.user,
            ).save()

    def remove_item(self, product) -> None:
        FavoriteProduct.objects.filter(id=product.id, user=self.user).delete()

    def clear(self) -> None:
        FavoriteProduct.objects.filter(user=self.user).delete()

    def get_products(self):
        return Product.objects.filter(favorite_products__user=self.user)


class WishListSession(WishList):
    """
    For anon users.
    """
    def __init__(self, session) -> None:
        self.session = session
        wish_list = self.session.get(settings.WISHLIST_SESSION_ID)
        if not wish_list:
            wish_list = {}
        self.wish_list = wish_list

    def append_item(self, product) -> None:
        self.wish_list[str(product.id)] = product.id
        self.save()

    def remove_item(self, product) -> None:
        del self.wish_list[str(product.id)]
        self.save()

    def clear(self) -> None:
        self.wish_list = {}
        self.save()

    def save(self) -> None:
        self.session.modified = True
        self.session[settings.WISHLIST_SESSION_ID] = self.wish_list

    def get_products(self):
        return Product.objects.filter(id__in=self.wish_list)

    def __iter__(self) -> int:
        for product_id in self.wish_list.values():
            yield product_id


def get_wish_list(request) -> WishList:
    if not request.user.is_authenticated:
        return WishListSession(request.session)
    return WishListDataBase(request.user)
