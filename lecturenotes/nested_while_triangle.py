rows = 5

i = 1
while i <= rows:  # i = row number
    j = 1
    while j <= i: # this loop prints *s, one at a time
        print("*", end="")
        j += 1
    print()
    i += 1
