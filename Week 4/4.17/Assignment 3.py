def day_num(day_name):
    names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if day_name in names:
        return names.index(day_name)
    else:
        return None


print(day_num("Monday"))
print(day_num("January"))
