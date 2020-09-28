A = float(input("Please enter the length of the horizontal size: "))
B = float(input("Please enter the length of the vertical size: "))

A_squared = A ** 2
B_squared = B ** 2

C_squared = A_squared + B_squared

C = C_squared ** 0.5

print("The length of the vertical side is ", C)