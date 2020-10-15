def slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)


print(slope(5, 3, 4, 2) == 1.0)
print(slope(1, 2, 3, 2) == 0.0)
print(slope(1, 2, 3, 3) == 0.5)
print(slope(2, 4, 1, 2) == 2.0)
