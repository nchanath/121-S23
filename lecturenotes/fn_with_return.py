def add(a,b):
    print("ADDING " + str(a) + " + " + str(b))
    return a+b

def subtract(a,b):
    print("SUBTRACTING " + str(a) + " - " + str(b))
    return a-b

def multiply(a,b):
    print("MULTIPLYING " + str(a) + " * " + str(b))
    return a*b

def divide(a,b):
    print("DIVIDING " + str(a) + " / " + str(b))
    return a/b

print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
shoe_size = divide(100,10)

print(f"Age: {age}, Height: {height}, Weight: {weight}, Shoe size: {shoe_size}")

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(shoe_size, 2))))

print(f"That becomes {what}. Can you do it by hand?")

