def outputCount(count):
    if count > 1:
        outputCount(count - 1)
    print(count)

outputCount(3)
