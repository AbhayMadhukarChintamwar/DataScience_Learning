from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass

class CoderPay(PaymentGateway):
    def pay(self):
        print('paying with CoderPay...')

class RazorPay:
    def pay(self):
        print('paying with RazorPay...')


class Purchase:
    def __init__(self, gateway):
        self.gateway = gateway

    def checkout(self):
        print('checking out...')
        self.gateway.pay()

gateway1 = RazorPay()
gateway2 = CoderPay()
purchase = Purchase(gateway2)

purchase.checkout()
