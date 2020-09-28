Numbers = [12, 3, 6, 8, 9, 23, 56, 23, 64]

sum = 0

for i in Numbers:
    if i % 2 == 0:
        sum = sum + i

first_even = 0
for i in Numbers:
    if i % 2 == 0:
        break
first_even = int(i)

print(sum - first_even)