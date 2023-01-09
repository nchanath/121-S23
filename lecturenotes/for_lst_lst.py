matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"The list of lists is {matrix}")
total = 0
for row in matrix:
    for value in row:
        print(f"Adding {value} to the total")
        total += value
print(f"The grand total is {total}.")
