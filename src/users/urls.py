from django.urls import path
from .views import (
    UserRegistrationView,
    SelfUserView,
    UserLogoutView,
    UserLogInView,
)

urlpatterns = [
    path('registration/', UserRegistrationView.as_view()),
    path('me/', SelfUserView.as_view()),
    path('login/', UserLogInView.as_view()),
    path('logout/', UserLogoutView.as_view()),
]
