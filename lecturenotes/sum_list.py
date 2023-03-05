def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        head = lst[0]
        tail = lst[1:]
        sum = head + sum_list(tail)
        print(f"sum = {sum}")
        return sum

print(f"sum_list[1,2,3] = {sum_list([1,2,3])}")
