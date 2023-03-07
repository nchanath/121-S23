class GiftCard:
    def __init__(self,amount):
        self.balance = amount

    def spend(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance = self.balance - amount
        return self.balance

    def addFunds(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def getBalance(self):
        return self.balance

