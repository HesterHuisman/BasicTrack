n = int(input("Please enter a number: "))

even_numbers = 0

for i in range(1, n+1):
    if i % 2 == 0:
        even_numbers = even_numbers + 1

for i in range(n-1, -1):
    if i % -2 == 0:
        even_numbers = even_numbers + 1

print(n, "contains", even_numbers, "even numbers")
