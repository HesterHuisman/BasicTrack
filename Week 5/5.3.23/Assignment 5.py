def add_vectors(vector1, vector2):
    """Add the numbers of lists with the same length"""
    new_list = []
    if len(vector1) == len(vector2):
        for index, var in enumerate(vector1):
            new_list.append(vector1[index] + vector2[index])
    return new_list


print(add_vectors([1, 1], [1, 1]))
print(add_vectors([1, 2], [1, 4]))
print(add_vectors([1, 2, 1], [1, 4, 3]))
