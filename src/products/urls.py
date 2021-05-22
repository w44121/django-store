from django.urls import path
from .views import (
    ProductListView,
    ProductRetrieveView,
    CategoryListView,
    ProducerListView,
    WishListView,
    WishListDetailView,
    SubscribeDetailView,
)
from social.views import ReviewView


urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductRetrieveView.as_view()),
    path('products/<int:product_id>/review/', ReviewView.as_view()),

    path('categories/', CategoryListView.as_view()),
    path('producers/', ProducerListView.as_view()),

    path('wishlist/', WishListView.as_view()),
    path('wishlist/<int:product_id>/', WishListDetailView.as_view()),

    path('products/<int:product_id>/subscribe/', SubscribeDetailView.as_view()),
]
