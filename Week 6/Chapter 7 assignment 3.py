with open("Story.txt", "r") as story:
    all_lines = story.readlines()
    g = open("Number_story.txt", "w")
    for i, v in enumerate(all_lines):
        i = str(i+1)
        j = str("0"*(4-len(i)) + i)
        b = j + " " + v
        g.write(b)

g.close()
