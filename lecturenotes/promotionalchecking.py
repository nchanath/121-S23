from checking import Checking

class PromotionalChecking(Checking):

    reward =  50

    def __init__(self,amount):
        Checking.__init__(self, amount + self.reward)
        # you could also write
        # super().__init__(amount + self.reward)

