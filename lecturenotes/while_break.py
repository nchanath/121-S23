# Good use of break statement in while loop
# Easy to tell the number of iterations
print("Good")

count = 0
while True:
    count += 1
    if count >= 10:
        break
    print(count)

# Output: 1 2 3 4 5 6 7 8 9

print()


# Bad use of break statement in while loop
# Harder to tell the number of iterations

print("Bad")

count = 0
while True:
    count += 1
    if count == 5:
        break
    print(count)

# Output: 1 2 3 4
