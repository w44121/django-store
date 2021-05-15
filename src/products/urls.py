from django.urls import path
from .views import (
    ProductList,
    CategoryList,
    ProducerList,
    WishListView,
    WishListDetailView,
    SubscribeView,
)


urlpatterns = [
    path('products/', ProductList.as_view()),
    path('categories/', CategoryList.as_view()),
    path('producers/', ProducerList.as_view()),

    path('wishlist/', WishListView.as_view()),
    path('wishlist/<int:product_id>/', WishListDetailView.as_view()),

    path('products/subscribe/', SubscribeView.as_view()),
]
