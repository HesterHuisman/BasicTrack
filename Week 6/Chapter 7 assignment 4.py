f = open("Number_story.txt")
lines_list = f.readlines()

new_list = []
for line in lines_list:
    new_line = line[2:]
    new_list.append(new_line)

g = open("No_number_story.txt", "w")

for line in new_list:
    g.write(line)

g.close()
