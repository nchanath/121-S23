def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        print(f"i={i}, result={result}")
    return result

def factorial_recursive(n):
    print(f"Computing factorial of {n}")
    if n == 0:
        print("returning 1")
        return 1
    else:
        result = n * factorial_recursive(n-1)
        print(f"returning {result}")
        return result


n = 3
print(f"\niterative factorial: {factorial_iterative(n)}") 
print()
print(f"\nrecursive factorial: {factorial_recursive(n)}") 
