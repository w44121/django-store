class OrderHasAlreadyBeenPaid(Exception):
    def __str__(self):
        return 'The order has already been paid'


class NotEnoughFundsForTheOperation(Exception):
    def __str__(self):
        return 'Not enough funds for  the operation.'


class BalanceReplenishmentWithANegativeValue(Exception):
    def __str__(self):
        return 'Balance replenishment with a negative value'
