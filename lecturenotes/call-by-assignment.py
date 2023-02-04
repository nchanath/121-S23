x = "out"
 
def foo(x):
    x = "in"
    print("local x: " + str(x))

print("global x: " + str(x))
foo(x)
print("global x: " + str(x))
print()

#################################################

y = [0,1,2]

def bar(y):
    y[1] = 7

print("y before: " + str(y))
bar(y)
print("y after: " + str(y))
print("Arrays are mutable.")
print()

#################################################

z = "hello"

def baz(z):
    z[0] = 'z'

print("z[0]: " + z[0])
baz(z)
