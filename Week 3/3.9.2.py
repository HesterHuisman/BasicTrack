number = int(input("Please enter a number: "))

prime = [True, False]

if number == 2:
    prime = True
elif number % 2 == 0:
    prime = False
elif number % 3 == 0:
    prime = False
elif number % 5 == 0:
    prime = False
elif number % 7 == 0:
    prime = False
elif number % 11 == 0:
    prime = False
else:
    prime = True

print(prime)