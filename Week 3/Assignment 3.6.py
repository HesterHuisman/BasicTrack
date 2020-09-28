numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in numbers:
    if i >= 75:
        print("First")
    elif i >= 70 and i < 75:
        print("Upper Second")
    elif i >= 60 and i < 70:
        print("Second")
    elif i >= 50 and i <60:
        print("Third")
    elif i >= 45 and i < 50:
        print("F1 Sup")
    elif i >= 40 and i < 45:
        print("F2")
    else:
        print("F3")

