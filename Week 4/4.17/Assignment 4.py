def day_add(weekday, days):
    names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if weekday in names:
        start_day = names.index(weekday)
        end_day_index = (start_day + days) % 7
        end_day = names[end_day_index]
        return end_day
    else:
        return None


print(day_add("Monday", 4))
print(day_add("Tuesday", 0))
print(day_add("Tuesday", 14))
print(day_add("Sunday", 100))
