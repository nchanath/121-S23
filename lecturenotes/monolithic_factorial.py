while True:
    number = int(input("Enter a positive integer: "))
    if number > 0:
        break
    else:
        print("Number must be positive.") 

factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1

print("The factorial of the number is ", factorial)
