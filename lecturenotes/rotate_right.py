def rotate_right(xs):
    if len(xs) > 1:
        last = xs.pop()
        xs.insert(0,last)
