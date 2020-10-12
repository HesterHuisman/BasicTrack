def rap_speed(words, seconds):
    """See if someone can rap faster than Eminem"""
    if words / seconds > 4.28:
        print("Sorry, you cannot rap faster than Eminem")
    else:
        print("You are the new rap god, ask Eminem for the crown")
    return ""


my_rap = (20, 3)

print(rap_speed(*my_rap))
