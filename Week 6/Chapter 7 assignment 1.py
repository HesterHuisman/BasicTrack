with open("storytime.txt", "r") as story:
    story_list = story.readlines()
    lines_list = story_list[0].split(".")
    for line in reversed(lines_list):
        print(line, end="")
