import random

def bubbleSort(aList):
    n = len(aList)
    for scan in range(1,n):
        i = 0
        while i < n - scan:
            if aList[i+1] < aList[i]:
                aList[i],aList[i+1] = aList[i+1],aList[i]
            i += 1

def merge(list1, list2):
    list = []
    index1 = 0
    index2 = 0
    n = len(list1) + len(list2)
    for index in range(n):
        if index2 >= len(list2):
            list.append(list1[index1])
            index1 += 1
        elif index1 >= len(list1):
            list.append(list2[index2])
            index2 += 1
        elif list1[index1] <= list2[index2]:
            list.append(list1[index1])
            index1 += 1
        else:
            list.append(list2[index2])
            index2 += 1
    return list

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
        sorted1 = mergeSort(list1)
        sorted2 = mergeSort(list2)
        # Combine them with merge.
        return merge(sorted1, sorted2)


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

def quickSort(someList):
    if len(someList) == 0:
        # It's already sorted! BASE CASE.
        return []
    else:
        smaller,pivot,larger = partition(someList)
        smallerSorted = quickSort(smaller)
        largerSorted = quickSort(larger)
        return smallerSorted + [pivot] + largerSorted


def part(someList,left,right):
    pivot = someList[left] # pick some value from the list
    i = left+1
    j = left+1
    while j <= right:
        x = someList[j]
        if x <= pivot:
            someList[i],someList[j] = someList[j],someList[i]
            i += 1
        j += 1
    middle = i-1
    someList[left], someList[middle] = someList[middle], someList[left]
    return middle

def qSortHelper(someList,left,right):
    if left <= right:
        between = part(someList,left,right)
        qSortHelper(someList, left, between-1)
        qSortHelper(someList, between+1, right)

def qSort(someList):
    qSortHelper(someList,0,len(someList)-1)
