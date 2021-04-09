from django.urls import path
from .views import (
    ProdcutList,
    CategoryList,
    ProducerList,
)


urlpatterns = [
    path('products/', ProdcutList.as_view()),
    path('categories/', CategoryList.as_view()),
    path('producers/', ProducerList.as_view()),
]
