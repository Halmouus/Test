#!/usr/bin/python3
"""1. Divide a matrix

Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats,
otherwise raise a TypeError exception with the message matrix
must be a matrix (list of lists) of integers/floats
Each row of the matrix must be of the same size, otherwise raise
a TypeError exception with the message Each row of the matrix
must have the same size
div must be a number (integer or float), otherwise raise a
TypeError exception with the message div must be a number
div cant be equal to 0, otherwise raise a ZeroDivisionError
exception with the message division by zero
All elements of the matrix should be divided by div, rounded
to 2 decimal places
Returns a new matrix"""


def matrix_divided(matrix, div):
    """function that divides contents of a matrix by an integer

    agruments: matrix(list of lists), div (non null integer)
    return: the new matrix
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
                         of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)\
                         of integers/floats")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)\
                         of integers/floats")
    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    n_matrix = []
    for row in matrix:
        n_row = []
        for i in row:
            j = round(i / div, 2)
            n_row.append(j)
        n_matrix.append(n_row)
    return (n_matrix)