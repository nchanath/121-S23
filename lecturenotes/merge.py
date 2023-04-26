def merge(list1, list2):
    lst = []

    while (list1 and list2): # list1 and list2 not empty
        head1 = list1[0]
        head2 = list2[0]

        if (head1 < head2):
            lst.append(head1)
            list1 = list1[1:]
        else:
            lst.append(head2)
            list2 = list2[1:]

    if (list1): # list1 still not empty
        lst += list1

    if (list2): # list2 still not empty
        lst += list2

    return lst


def oldmerge(list1, list2):
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
        
        # Sort each half.
        sorted1 = mergeSort(someList[:n//2])
        sorted2 = mergeSort(someList[n//2:])
        
        # Combine them with merge.
        return merge(sorted1, sorted2)

                     
l = [87,3,56,9,2,10,38]
print(f"original list: {l}")

ll = mergeSort(l)
print(f"sorted list: {ll}")
