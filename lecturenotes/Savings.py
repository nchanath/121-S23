class Savings(Account):
    interest_rate = 0.04
    withdraw_fee = 1.0
    
    def withdraw(self,amount):
        Account.withdraw(self, amount + self.withdraw_fee)
