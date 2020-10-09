def remove(part, phrase):
    new_word = ""
    n = phrase.find(part)
    print("n=", n)
    m = n + len(part)
    print("m=", m)
    for index, letter in enumerate(phrase):
        print(index)
        if index < n:
            new_word = new_word + letter
            print(new_word)
    for index, letter in enumerate(phrase):
        if index > m:
            new_word = new_word + letter
    return new_word


remove(remove("an", "banana"))
