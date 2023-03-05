def outputCount(count):
    print(count)
    if count > 1:
        outputCount(count - 1)

outputCount(3)
