def getArea():
    a = float(input("Circle area? "))
    while a < 0.0:
        a = float(input("Not an area. Try again:"))
    return a

def radiusOfCircle(someArea):
    from math import pi, sqrt
    return sqrt(someArea / pi)

area = getArea()
radius = radiusOfCircle(area)
print(str(pi))
print("That circle\'s radius is "+str(radius)+".")
