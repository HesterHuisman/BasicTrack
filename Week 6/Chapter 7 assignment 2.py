with open("Snake.txt", "r") as story:
    for line in story:
        if "snake" in line:
            print(line, end="")
