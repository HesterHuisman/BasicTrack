def f2c(t):
    return round((t - 32) / 1.8)


print(f2c(212) == 100)
print(f2c(32) == 0)
print(f2c(-40) == -40)
print(f2c(36) == 2)
print(f2c(37) == 3)
print(f2c(38) == 3)
print(f2c(39) == 4)
