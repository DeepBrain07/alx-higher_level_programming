#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            j = 1
            for k in i:
                if j != len(i):
                    print("{:d}".format(j), end=' ')
                else:
                    print("{:d}".format(j))
                j += 1
