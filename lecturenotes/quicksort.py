def quickSort(someList):
    if len(someList) == 0:
        # It's already sorted! BASE CASE.
        return []
    elif len(someList) == 1:
        return [someList[0]]
    else:
        smaller,pivot,larger = partition(someList)

        smallerSorted = quickSort(smaller)
        largerSorted = quickSort(larger)
        return smallerSorted + [pivot] + largerSorted

def partition(someList):
    pivot = someList[0] # pick some value from the list
    smallers = []
    largers = []
    for x in someList[1:]:
        if x <= pivot:
            smallers.append(x)
        else:
            largers.append(x)
    return smallers, pivot, largers


l = [40, 22,60,3,65,87,14]
print(f"original list: {l}")
print()

ll = quickSort(l)
print()
print(f"sorted list: {ll}")
