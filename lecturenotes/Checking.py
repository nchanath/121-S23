class Checking(Account):
    min_balance = 1000.0

    def payInterest(self):
        if self.balance >= self.min_balance:
            Account.payInterest(self)
    
