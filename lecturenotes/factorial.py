def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        print(f"i={i}, result={result}")
    return result

def factorial_recursive(n):
    if n == 0:
        print(f"factorial_recursive({n}) = 1")
        return 1
    else:
        print(f"factorial_recursive({n}) = {n} * factorial_recursive({n-1})")
        result = n * factorial_recursive(n-1)
        print(f"result for n = {n} is {result}")
        return result


n = 5
print(f"\niterative factorial: {factorial_iterative(n)}") # prints 120
print()
print(f"\nrecursive factorial: {factorial_recursive(n)}") # prints 120
