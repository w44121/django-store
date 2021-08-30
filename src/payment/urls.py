from django.urls import path
from payment.views import (
    WalletUserView,
    TransactionUserView,
    OrderPaymentView,
)


urlpatterns = [
    path('api/user/me/wallet/', WalletUserView.as_view()),
    path('api/user/me/transations/', TransactionUserView.as_view()),

    path('api/orders/<int:order_id>/pay/', OrderPaymentView.as_view()),
]
