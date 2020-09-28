Side_1 = float(input("Please enter the length of the first side: "))
Side_2 = float(input("Please enter the length of the second side: "))
Side_3 = float(input("Please enter the length of the third side: "))

A = (Side_2**2 + Side_3**2)**0.5
B = (Side_1**2 + Side_3**2)**0.5
C = (Side_1**2 + Side_2**2)**0.5

threshold = 1e-7

print(abs(Side_1 - A) < threshold or abs(Side_2 - B) < threshold or abs(Side_3 - C) < threshold)