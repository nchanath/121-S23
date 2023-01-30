a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a > b and a > c:
    print("a is the largest")
elif b > a and b > c:
    print("b is the largest")
else:
    print("c is the largest")