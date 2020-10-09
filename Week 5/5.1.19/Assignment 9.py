def remove_letter(the_letter, word):
    new_word = ""
    for letter in word:
        if letter.lower() != the_letter:
            new_word += letter
    return new_word


print(remove_letter("a", "apple"))
print(remove_letter("a", "banana"))
print(remove_letter("z", "banana"))
print(remove_letter("i", "Mississippi"))
print(remove_letter("b", ""))
print(remove_letter("b", "c"))
