def merge(list1, list2):
    lst = []
    index1 = 0
    index2 = 0
    n = len(list1) + len(list2)
    for index in range(n):
        if index2 >= len(list2):
            lst.append(list1[index1])
            index1 += 1
        elif index1 >= len(list1):      
            lst.append(list2[index2])
            index2 += 1
        elif list1[index1] <= list2[index2]:
            lst.append(list1[index1])
            index1 += 1
        else:
            lst.append(list2[index2])
            index2 += 1
    return lst

def mergeSort(someList):
    if len(someList) <= 1:
        # It's already sorted! BASE CASE.
        return someList
    else:
        # It's larger and needs more work. RECURSIVE CASE.
        n = len(someList)
        
        # Split into two halves.
        list1 = someList[:n//2]
        list2 = someList[n//2:]
        
        # Sort each half.
        print(f"Sorting {list1} and {list2}")
        sorted1 = mergeSort(list1)
        sorted2 = mergeSort(list2)
        
        # Combine them with merge.
        return merge(sorted1, sorted2)

                     
l = [87,3,56,9,2,10,38]
print(f"original list: {l}")

ll = mergeSort(l)
print(f"sorted list: {ll}")
