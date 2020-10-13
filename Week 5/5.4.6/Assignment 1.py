letter_counts = {}

sentence = "ThiS is String with Upper and lower case Letters"
sentence = "".join(sentence.split())

for letter in sentence:
    letter = letter.lower()
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

letter_items = list(letter_counts.items())
letter_items.sort()

for key, value in letter_items:
    print(key, ' ', value, '\t')
