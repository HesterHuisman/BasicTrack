def hours_in(secs):
    return secs // 3600


def minutes_in(secs):
    return (secs % 3600) // 60


def seconds_in(secs):
    return secs % 60


print(hours_in(9010))
print(minutes_in(9010))
print(seconds_in(9010))
