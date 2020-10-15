def turn_clockwise(compass_point):
    points = ["N", "E", "S", "W"]
    for i, v in enumerate(points):
        if compass_point == v:
            a = points[(i+1) % len(points)]
            return a
    else:
        return None


print(turn_clockwise("N"))
print(turn_clockwise("W"))
print(turn_clockwise("C"))
