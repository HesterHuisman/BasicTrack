def to_secs(hours, minutes, secs):
    return int(hours*3600 + minutes*60 + secs)


print(to_secs(2.5, 0, 10.71))
print(to_secs(2.433, 0, 0))
