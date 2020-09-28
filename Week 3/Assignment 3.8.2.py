n = int(input("Please enter how many triangular numbers you want: "))

print(range(1, n))

for i in range(1, n+1):
    triangular = i * (i + 1) / 2
    print(i, '\t' ,triangular, end= '\n')