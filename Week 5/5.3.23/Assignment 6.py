def scalar_mult(scalar, vector):
    """Return the multiple of a vector by a scalar"""
    new_list = []
    for element in vector:
        new_list.append(scalar*element)
    return new_list


print(scalar_mult(5, [1, 2]))
print(scalar_mult(3, [1, 0, -1]))
print(scalar_mult(7, [3, 0, 5, 11, 2]))
