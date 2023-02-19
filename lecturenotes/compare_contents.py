def same_contents(xs,ys):
    if len(xs) != len(ys):
        return False
    i = 0
    while i < len(xs):
        if xs[i] != ys[i]:
            return False
        i = i + 1
    return True
