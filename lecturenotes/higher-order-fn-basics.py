# functions can be assigned to variables

def greet(name):
    print(f"Hello, {name}!")

hello = greet
hello("Alice")


# functions can be passed as arguments to other functions

def apply(func, arg):
    return func(arg)

def double(x):
    return x * 2

print(apply(double, 5))


# functions can be returned from other functions

def create_multiplier(x):
    def multiplier(y):
        return x * y
    return multiplier

mult5 = create_multiplier(5)
mult10 = create_multiplier(10)

print(mult5(3))
print(mult10(3))


# functions can be stored in data structures

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

operations = [square, cube]

for operation in operations:
    print(operation(3))


# functions can be created dynamically

def create_function(n):
    def new_function(x):
        return x ** n
    return new_function

square = create_function(2)
cube = create_function(3)

print(square(3))
print(cube(3))


# functions can be used as return values

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add3 = make_adder(3)
add5 = make_adder(5)

def apply_operation(numbers, operation):
    result = []
    for number in numbers:
        result.append(operation(number))
    return result

numbers = [1, 2, 3, 4, 5]
print(apply_operation(numbers, add3))
print(apply_operation(numbers, add5))




#  
# Exercises
#
# 1.  Create a function `compose` that takes two functions `f` and `g` as arguments and returns a new function that applies `f` to the result of `g`.
#
#     For example, if `f` is the `square` function and `g` is the `add3` function that adds `3` to its argument, the composed function should apply `square` to the result of `add3`. Use this composed function to calculate the square of `7` after adding `3` to it.

def compose(f, g):
    pass

#   
#  
# 2.  Create a function `apply_function` that takes a function `f` and a list `lst` as arguments and applies `f` to each element of `lst`, returning a list of the results.
#
#     For example, if `f` is the `cube` function and `lst` is `[1, 2, 3]`, the result should be `[1, 8, 27]`. Use this function to calculate the sum of the cubes of the numbers from `1` to `5`.

def apply_function(f, lst):
    pass

#  
#  
# 3.  Create a function `filter_function` that takes a function `f` and a list `lst` as arguments and returns a new list containing only the elements of `lst` for which `f` returns `True`.
#
#     For example, if `f` is the `is_even` function that returns `True` if its argument is even, and `lst` is `[1, 2, 3, 4, 5]`, the result should be `[2, 4]`. Use this function to find all the prime numbers between `1` and `20`.

def filter_function(f, lst):
    pass

