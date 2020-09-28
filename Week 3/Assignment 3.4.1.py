numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# a. Write a loop that prints each of the numbers on a new line.
for i in numbers:
    print(i, end='\n')

# b. Write a loop that prints each number and its square on a new line.
for i in numbers:
    print(i, '\t', i**2, end='\n')

# c. Write a loop that adds all the numbers from the list into a variable called total.
# You should set the total variable to have the value 0 before you start adding them up,
# and print the value in total after the loop has completed.
total = 0

for i in numbers:
    total += i
print(total)

# d. Print the product of all the numbers in the list. (product means all multiplied together)
result = 1
for i in numbers:
    result = result * i
print(result)
