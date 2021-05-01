from django.conf import settings
# from .models import FavoriteProduct


class WishListSession:
    def __init__(self, session):
        self.session = session
        wish_list = self.session.get(settings.WISHLIST_SESSION_ID)
        if not wish_list:
            wish_list = {}
        self.wish_list = wish_list

    def append_item(self, product):
        self.wish_list[str(product.id)] = product.id
        self.save()

    def remove_item(self, product):
        del self.wish_list[str(product.id)]
        self.save()

    def clear(self):
        self.wish_list = {}
        self.save()

    def save(self):
        self.session.modified = True
        self.session[settings.WISHLIST_SESSION_ID] = self.wish_list

    def __iter__(self):
        for value in self.wish_list.values():
            yield value
