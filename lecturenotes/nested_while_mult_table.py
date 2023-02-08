i = 1
while i < 11:
    j = 1
    row = ""
    while j < 11:
        row += str(i * j) + "\t"
        j += 1
    print(row)
    i += 1
