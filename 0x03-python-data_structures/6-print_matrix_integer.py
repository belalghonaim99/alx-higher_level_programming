#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for c in x:
            print("{:d}".format(c), end=" " if c != x[-1] else "")
        print()
