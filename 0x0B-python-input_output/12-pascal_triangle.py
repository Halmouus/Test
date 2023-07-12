#!/usr/bin/python3
"""12. Pascal's Triangle

function that that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """function that that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                calc = triangle[i-1][j-1] + triangle[i-1][j]
                row.append(calc)
        triangle.append(row)
    return triangle