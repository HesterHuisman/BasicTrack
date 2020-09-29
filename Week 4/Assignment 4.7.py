def sum_to(n):
    """Sum of all integer numbers"""
    sum_var = 0
    for i in range(1, n+1):
        sum_var = sum_var + i
    return sum_var


print(sum_to(10))
