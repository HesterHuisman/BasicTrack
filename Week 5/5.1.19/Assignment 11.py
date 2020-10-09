def count(part, phrase):
    times_in_word = 0
    index = 0
    for letter in phrase:
        if phrase.find(part, index) > 0:
            times_in_word += 1
            index = phrase.find(part, index) + 1
        else:
            break
    return times_in_word


print(count("is", "mississippi") == 2)
print(count("an", "banana") == 2)
print(count("ana", "banana") == 2)
print(count("nana", "banana") == 1)
print(count("nanan", "banana") == 0)
print(count("aaa", "aaaaaa") == 4)
