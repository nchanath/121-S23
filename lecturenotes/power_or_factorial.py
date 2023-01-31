def get_user_input():
    user_input = input("Do you want to compute 2^n or n!? (Type 'p' for 2^n or 'f' for n!) ")
    if user_input == 'p':
        return 'p'
    elif user_input == 'f':
        return 'f'
    else:
        print("Invalid input. Please try again.")
        return get_user_input()

def get_number():
    number = int(input("Enter a positive integer: "))
    if number < 0:
        print("Number must be positive.")
        return get_number()
    return number

def calculate_2_to_the_n(number):
    result = 2 ** number
    return result

def calculate_factorial(number):
    result = 1
    i = 1
    while i <= number:
        result *= i
        i += 1
    return result

def display_result(result):
    print("The result is:", result)

user_input = get_user_input()
number = get_number()

if user_input == 'p':
    result = calculate_2_to_the_n(number)
else:
    result = calculate_factorial(number)

display_result(result)
