class Account:

    interest_rate = .02

    def __init__(self,amount):
        self.balance = amount

    def deposit(self,amount):
        self.balance += amount

    def payInterest(self):
        self.balance *= 1.0 + self.interest_rate

    def getBalance(self):
        return self.balance
