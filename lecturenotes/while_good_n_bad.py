# Good use of while loop
# Easy to tell what the stop condition is

print("Good")

count = 0
while count < 10:
    count += 1
    print(count)

# Output: 1 2 3 4 5 6 7 8 9 10

print()



# Bad use of while loop (infinite loop)
# Hard to tell what the stop condition is

print("Bad")

count = 0
while True:
    count += 1
    print(count)
    if count >= 10:
        break
