def divisor_list(number):
    divisors = []
    d = 1
    while d <= number:
        if number % d == 0:
            divisors.append(d)
        d += 1
    return divisors
