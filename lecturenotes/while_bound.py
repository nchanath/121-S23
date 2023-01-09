while True:
    user_input = int(input("Enter a number: "))
    if user_input > 100:
        print("Number is greater than 100!")
        break
    else:
        print("Number is less than or equal to 100. Try again.")
