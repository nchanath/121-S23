def count_x(s):
    if len(s) == 0:
        return 0
    elif s[0] == 'x':
        return 1 + count_x(s[1:])
    else:
        return count_x(s[1:])

print(count_x('hello'))
print(count_x('xerox'))
