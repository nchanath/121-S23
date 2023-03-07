def createGiftCard(amount):
    return {"balance": amount}

def spend(giftCard, amount):
    balance = giftCard["balance"]
    if amount > balance:
        return "Insufficient funds"
    balance -= amount

    giftCard["balance"] = balance
    return balance

def addFunds(giftCard, amount):
    giftCard["balance"] += amount
    return giftCard["balance"]


