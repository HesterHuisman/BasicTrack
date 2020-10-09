word = "banana"


def count_letters(the_string, the_letter, start=0):
    """Function that counts the number of times a letter is in a string"""
    count = 0
    for index, letter in enumerate(the_string[start:]):
        if letter == the_letter:
            count += 1
    return count


print(count_letters(word, 'a'))
