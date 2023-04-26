def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
                print(f"{l}")
            else:
                break

l = [87,3,56,9,2,10,38]
print(f"{l}")

insertion_sort(l)
print(f"{l}")
