from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from payment.models import Wallet, Transaction
from payment.serializers import WalletSerializer, TransactionSerializer
from payment.controller import get_wallet, WalletController, OrderPayment
from payment.errors import (
    OrderHasAlreadyBeenPaid,
    NotEnoughFundsForTheOperation,
    BalanceReplenishmentWithANegativeValue,
)
from orders.models import Order


class WalletUserView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        wallet = get_wallet(request.user)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)
    
    def post(self, request):
        try:
            amount = request.data.get('amount')
            wallet = WalletController(request.user)
            wallet.up_balance(amount)
            serializer = WalletSerializer(wallet.wallet)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TransactionUserView(ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)


class OrderPaymentView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, order_id):
        try:
            user = request.user
            order = Order.objects.get(id=order_id)
            OrderPayment(user, order).pay()
            return Response(status=status.HTTP_200_OK)
        except (
            BalanceReplenishmentWithANegativeValue,
            NotEnoughFundsForTheOperation,
            OrderHasAlreadyBeenPaid,
        ) as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
