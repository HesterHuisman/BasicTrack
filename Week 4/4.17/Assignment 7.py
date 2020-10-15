def to_secs(hours, minutes, secs):
    return hours*3600 + minutes*60 + secs


print(to_secs(2, 30, 10) == 9010)
print(to_secs(2, 0, 0) == 7200)
print(to_secs(0, 2, 0) == 120)
print(to_secs(0, 0, 42) == 42)
print(to_secs(0, -10, 10) == -590)
