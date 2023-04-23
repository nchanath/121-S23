def quickSort(someList):
    if len(someList) == 0:
        # It's already sorted! BASE CASE.
        return []
    else:
        smaller,pivot,larger = partition(someList)

        print(f"pivot = {pivot} \t sorting {smaller} and {larger}")

        smallerSorted = quickSort(smaller)
        largerSorted = quickSort(larger)
        return smallerSorted + [pivot] + largerSorted

def partition(someList):
    smallers = []
    pivot = someList[0] # pick some value from the list
    largers = []
    for x in someList[1:]:
        if x <= pivot:
            smallers.append(x)
        else:
            largers.append(x)
    return smallers, pivot, largers


l = [40, 22,60,3,65,87,14,56,30,100,33,9]
print(f"original list: {l}")
print()

ll = quickSort(l)
print()
print(f"sorted list: {ll}")
