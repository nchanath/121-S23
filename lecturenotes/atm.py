balance = 1000
withdrawal_limit = 500

while True:
    print("Welcome to the ATM!")
    print("Your current balance is:", balance)
    withdrawal_amount = int(input("Enter the amount you want to withdraw (0 to exit): "))
    if withdrawal_amount == 0:
        print("Thank you for using our ATM. Have a great day!")
        break
    elif withdrawal_amount > balance:
        print("Insufficient balance, please try again")
    elif withdrawal_amount > withdrawal_limit:
        print("Exceeded withdrawal limit, please try again")
    else:
        balance -= withdrawal_amount
        print("Please take your cash")
