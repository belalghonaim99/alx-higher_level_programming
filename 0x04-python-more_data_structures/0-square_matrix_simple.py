#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for y in range(len(matrix)):
        new_matrix[y] = list(map(lambda x: x**2, matrix[y]))
    return (new_matrix)
