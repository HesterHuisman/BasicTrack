def replace(s, old, new):
    new_list = s.split(old)
    glue = new
    s = glue.join(new_list)
    return s


print(replace("Mississippi", "i", "I"))
song = "I love spom! Spom is my favorite food. Spom, spom, yum!"
print(replace(song, "om", "am"))
print(replace(song, "o", "a"))
