Numbers = [12, 3, 6, 8, -9, -73, 56, -23, 64]

count = 0

for i in Numbers:
    if i < 0:
        count = count + i

print(count)
