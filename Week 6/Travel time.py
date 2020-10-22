mode_time = {"walking": 20, "biking": 5, "car": 1}
#  only one change to add another mode of transportation: add mode to the mode_time dictionary


def travel_time(mode, km):
    """Estimate the travel time using a certain mode of transportation"""
    for key, time in mode_time.items():
        if mode == key:
            speed = km * time
    get_going = int(input("How many minutes does it take for this mode of transportation to get going? "))
    parking = int(input("How many minutes does it take for this mode of transportation to park? "))
    speed = speed + get_going + parking
    hours = speed // 60
    minutes = speed % 60
    return print("Your travel time is ", hours, "hours and ", minutes, "minutes")


travel_time("biking", 10)


