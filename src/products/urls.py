from django.urls import path
from .views import (
    ProdcutList,
    CategoryList,
    ProducerList,
    WishListView,
    WishListDetailView,
)


urlpatterns = [
    path('products/', ProdcutList.as_view()),
    path('categories/', CategoryList.as_view()),
    path('producers/', ProducerList.as_view()),

    path('wishlist/', WishListView.as_view()),
    path('wishlist/<int:product_id>/', WishListDetailView.as_view()),
]
