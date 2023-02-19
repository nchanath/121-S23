def is_palindrome(xs):
    hi = len(xs)-1
    lo = 0
    while hi > lo:
        if xs[lo] != xs[hi]:
            return False
        lo = lo + 1
        hi = hi - 1
    return True
