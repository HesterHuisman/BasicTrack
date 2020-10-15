def day_name(number):
    names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if number in range(6):
        return names[number]
    else:
        return None


print(day_name(0))
print(day_name(5))
print(day_name(7))
