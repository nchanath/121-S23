def fib_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
            print(f"fib[{i}] = fib[{i-1}] + fib[{i-2}] = {fib[i-1]} + {fib[i-2]} = {fib[i]}")
        return fib[n]

def fib_recursive(n):
    print(f"fib_recursive({n})")
    if n <= 1:
        return n
    fib_n_minus_1 = fib_recursive(n-1)
    fib_n_minus_2 = fib_recursive(n-2)
    fib_n = fib_n_minus_1 + fib_n_minus_2
    print(f"fib_n_minus_1 of {n} = {fib_n_minus_1}")
    print(f"fib_n_minus_2 of {n} = {fib_n_minus_2}")
    print(f"fib_recursive({n}) = {fib_n}")
    return fib_n
    

n = 4
print(f"\niterative fib: {fib_iterative(n)}")
print()
print(f"\nrecursive fib: {fib_recursive(n)}")


##################################################

def fib_recursive_i(n, depth=0):
    print("  " * depth, f"fib_recursive_i({n})")
    if n <= 1:
        return n
    fib_n_minus_1 = fib_recursive_i(n-1, depth+1)
    fib_n_minus_2 = fib_recursive_i(n-2, depth+1)
    fib_n = fib_n_minus_1 + fib_n_minus_2
    print("  " * (depth+1), f"fib_n_minus_1 of {n} = {fib_n_minus_1}")
    print("  " * (depth+1), f"fib_n_minus_2 of {n} = {fib_n_minus_2}")
    print("  " * depth, f"fib_recursive_i({n}) = {fib_n}")
    return fib_n
