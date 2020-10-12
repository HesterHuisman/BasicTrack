def dot_product(vec1, vec2):
    """take two lists of numbers of the same length, and return the sum of the products of the
    corresponding elements of each"""
    new_list = []
    sum = 0
    if len(vec1) == len(vec2):
        for i, v in enumerate(vec1):
            new_list.append(vec1[i] * vec2[i])
    for element in new_list:
        sum = sum + element
    return sum


print(dot_product([1, 1], [1, 1]))
print(dot_product([1, 2], [1, 4]))
print(dot_product([1, 2, 1], [1, 4, 3]))
