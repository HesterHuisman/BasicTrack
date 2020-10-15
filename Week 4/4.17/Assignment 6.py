def days_in_month(month):
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
               "October", "November", "December"]
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month in month_names:
        a = month_names.index(month)
        return month_days[a]
    else:
        return None


print(days_in_month("February"))
print(days_in_month("December"))
