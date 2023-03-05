def outputCountTweaked(count):
    print(count)
    if count > 1:
        outputCountTweaked(count - 1)
    print(count)

outputCountTweaked(3)
