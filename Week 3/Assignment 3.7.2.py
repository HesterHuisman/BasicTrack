n = float(input("Please enter the number you want to estimate the square root of: "))
approximation = n/2

better = 0
threshold = 0.001

while True:
    better = (approximation + n / approximation) / 2
    print(better, end='\n')
    if abs(approximation - better) < threshold:
        break
    approximation = better
