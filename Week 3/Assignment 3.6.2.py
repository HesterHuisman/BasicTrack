Words = ["Frodo", "and", "sam", "are", "walking", "to", "mordor"]

word_count = 0

for i in Words:
    word_count = word_count + 1
    if i == "sam":
        break

if word_count == len(Words):
    word_count = 0

print(word_count)
