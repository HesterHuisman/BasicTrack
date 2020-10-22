f = open("Number_story.txt")
lines_list = f.readlines()

g = open("No_number_story.txt", "w")
new_list = []
for line in lines_list:
    new_line = line[5:]
    g.write(new_line)

g.close()
