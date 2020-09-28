Side_1 = float(input("Please enter the length of the vertical side: "))
Side_2 = float(input("Please enter the length of the horizontal side: "))
Side_3 = float(input("Please enter the length of the diagonal side: "))

C_squared = Side_1**2 + Side_2**2
C = C_squared**0.5

threshold = 1e-7

print(abs(Side_3 - C) < threshold)