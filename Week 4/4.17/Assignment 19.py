def c2f(t):
    return round((t * 1.8) + 32)


print(c2f(0) == 32)
print(c2f(100) == 212)
print(c2f(-40) == -40)
print(c2f(12) == 54)
print(c2f(18) == 64)
print(c2f(-48) == -54)
