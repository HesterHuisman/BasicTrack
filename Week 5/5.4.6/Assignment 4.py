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

list_length = sorted(word_counts.items(),  key=lambda x: len(x[0]))
print(len(list_length[-1][0]))
