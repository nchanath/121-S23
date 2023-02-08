rows = 5

i = 1
while i <= rows:         # print one row at a time; i is the row number
    k = 1
    while k <= rows - i: # this loop prints white spaces, one at a time
        print(" ", end="")
        k += 1
    j = 1
    while j <= i:        # this loop prints numbers, one at a time
        print(j, end="")
        j += 1
    print()
    i += 1
