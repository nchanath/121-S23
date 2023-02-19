def contains(y,xs):
    i = 0
    while i < len(xs):
        if xs[i] == y:
            return True
        i = i + 1
    return False
