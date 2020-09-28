weekdays = [(0, "Sunday"), (1, "Monday"), (2, "Tuesday"), (3, "Wednesday"), (4, "Thursday"), (5, "Friday"), (6, "Saturday")]

start_day = int(input("What is the number of the start day?: "))
stay_length = int(input("What is the length of your stay in days?: "))

end_day = (start_day + stay_length) % 7

for number, day in weekdays:
    if end_day == number:
        print(day)
