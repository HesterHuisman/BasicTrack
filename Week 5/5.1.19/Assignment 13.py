def remove(part, word):
    """remove part from word"""
    n = word.find(part)
    m = len(part)
    new_word = ""
    while True:
        part in word
        part1 = word[:n]
        part2 = word[m+1:]
        new_word = part1 + part2
        word = new_word
        if part not in word:
            break
    new_word = word
    return new_word


print(remove("an", "banana"))
print(remove("cyc", "bicycle"))
print(remove("iss", "Mississippi"))
print(remove("eggs", "bicycle"))
# last one is not working :(
