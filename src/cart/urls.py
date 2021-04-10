from django.urls import path
from .views import (
    CartView,
    CartDetailView,
)


urlpatterns = [
    path('', CartView.as_view()),
    path('<int:product_id>/', CartDetailView.as_view()),
]
