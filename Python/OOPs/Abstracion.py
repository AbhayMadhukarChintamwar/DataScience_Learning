


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
purchase1 = Purchase(gateway1)
purchase1.checkout()
