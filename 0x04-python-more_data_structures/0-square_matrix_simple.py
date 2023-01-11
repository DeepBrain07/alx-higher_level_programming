#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_matrix.append(i)
    for i in range(len(new_matrix)):
        new_matrix2 = []
        for j in new_matrix[i]:
            new_matrix2.append(j*j)
        new_matrix[i] = new_matrix2
    return new_matrix            
