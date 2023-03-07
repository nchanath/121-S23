class Account:

    rate = .02

    def __init__(self,amount):
        self.balance = amount

    def deposit(self,amount):
        self.balance += amount

    def payInterest(self):
        self.balance *= 1.0 + rate

    def spend(self, amount):
        return

    def transferTo(self, receiver):
        return
