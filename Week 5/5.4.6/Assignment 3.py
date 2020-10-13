import string


def remove_punctuation(phrase):
    phrase_sans_punct = ""
    for letter in phrase:
        if letter not in string.punctuation:
            phrase_sans_punct += letter
    return phrase_sans_punct


f = open('alice.txt', 'r')
content = f.read()
content = ''.join([i for i in content if not i.isdigit()])
words = remove_punctuation(content).split()


word_counts = {}

for word in words:
    word = word.lower()
    word_counts[word] = word_counts.get(word, 0) + 1

word_items = list(word_counts.items())
word_items.sort()


a = "Word" + " "*15 + "Count"

g = open("alice_words.txt", "w")
g.write(a)
g.write('\n')
g.write("="*24)
g.write('\n')

for (key, value) in word_items:
    value = str(value)
    space_bars = 19 - len(key)
    b = key + " " * space_bars + value
    g.write(b)
    g.write('\n')

g.close()
