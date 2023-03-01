# Iterative solution
def sum_iterative(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

# Recursive solution
def sum_recursive(n):
    print(f"Computing sum_recursive({n})")
    if n == 0:
        print(f"sum_recursive({n}) = 0")
        return 0
    result = n + sum_recursive(n-1)
    print(f"sum_recursive({n}) = {n} + sum_recursive({n-1}) = {result}")
    return result

def sum_recursive_i(n, depth=0):
    print("  " * depth, f"Computing sum_recursive_i({n})")
    if n == 0:
        print("  " * depth, f"sum_recursive_i({n}) = 0")
        return 0
    result = n + sum_recursive_i(n-1, depth+1)
    print("  " * depth, f"sum_recursive_i({n}) = {n} + sum_recursive_i({n-1}) = {result}")
    return result

# Test the functions
n = 3
print(f"Sum of 0 to {n} (iterative): {sum_iterative(n)}\n")
print()
print(f"Sum of 0 to {n} (recursive): {sum_recursive(n)}")
print()
print(f"Sum of 0 to {n} (recursive): {sum_recursive_i(n)}")
