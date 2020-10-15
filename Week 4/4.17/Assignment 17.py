def is_factor(f, n):
    return n % f == 0


def is_multiple(n, f):
    return is_factor(f, n)


print(is_multiple(12, 3))
print(is_multiple(12, 4))
print(not is_multiple(12, 5))
print(is_multiple(12, 6))
print(not is_multiple(12, 7))
