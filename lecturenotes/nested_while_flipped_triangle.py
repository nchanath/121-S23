rows = 5

i = 1
while i <= rows: # i = row number
    k = rows - i 
    while k > 0: # this loop prints the white spaces, one at a time
        print(" ", end="")
        k -= 1
    j = 1
    while j <= i: # this loop prints the *s, one at a time
        print("*", end="")
        j += 1
    print()
    i += 1
