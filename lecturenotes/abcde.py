def abcde(op,size):
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            value = op(i,j)
            print(str(value),end=‘\t’)
            j = j + 1
        print()
        i = i + 1
