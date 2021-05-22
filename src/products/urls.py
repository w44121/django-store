from django.urls import path
from .views import (
    ProductList,
    ProductRetrieveView,
    CategoryList,
    ProducerList,
    WishListView,
    WishListDetailView,
    SubscribeDetailView,
)
from social.views import ReviewView


urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductRetrieveView.as_view()),
    path('products/<int:product_id>/review/', ReviewView.as_view()),

    path('categories/', CategoryList.as_view()),
    path('producers/', ProducerList.as_view()),

    path('wishlist/', WishListView.as_view()),
    path('wishlist/<int:product_id>/', WishListDetailView.as_view()),

    path('products/<int:product_id>/subscribe/', SubscribeDetailView.as_view()),
]
