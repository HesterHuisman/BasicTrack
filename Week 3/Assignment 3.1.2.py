Numbers = [12, 3, 6, 8 , 9, 23 ,56, 23, 64]

count = 0

for i in Numbers:
    if i % 2 == 0:
        count = count + 1

print(count)