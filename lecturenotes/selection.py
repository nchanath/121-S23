def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        print(f"min_val = {lst[i]}")

        for j in range(i+1, n): # scan the list from i+1st element on for a minimum
            if lst[j] < lst[min_idx]:
                min_idx = j
                print(f"min_val = {lst[j]}")

        lst[i], lst[min_idx] = lst[min_idx], lst[i] 
        print(f"{lst}")

    return lst


l = [87,3,56,9,2,10,38]
print(f"original list = {l}")
selection_sort(l)
print(f"sorted list = {l}")
