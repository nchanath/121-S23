def tablePrinterFor(op):
    def printTable(rows,cols):
        for i in range(rows):
            for j in range(cols):
                value = op(i,j)
                print(value,end='\t')
            print()
    return printTable
