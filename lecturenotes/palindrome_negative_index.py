def is_palindrome(xs):
    index = 0
    middle = len(xs) // 2
    while index < middle:
        if xs[index] != xs[-(index+1)]:
            return False
        index = index + 1
    return True
