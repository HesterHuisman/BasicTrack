def is_odd(n):
    return n % 2 != 0


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return not is_even(n)


print(is_odd(7))
print(is_odd(6))
