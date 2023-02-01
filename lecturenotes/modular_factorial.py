def get_number():
    number = int(input("Enter a positive integer: "))
    if number < 0:
        print("Number must be positive.")
        return get_number()
    return number

def calculate_factorial(number):
    result = 1
    i = 1
    while i <= number:
        result *= i
        i += 1
    return result


def display_factorial(factorial):
    print("The factorial of the number is:", factorial)

number = get_number()
factorial = calculate_factorial(number)
display_factorial(factorial)
