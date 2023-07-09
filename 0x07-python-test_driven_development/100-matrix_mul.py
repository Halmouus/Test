#!/usr/bin/python3
"""Module of matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices

    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    for row in m_a:
        if not (len(row) == len(m_a[0])):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if not (len(row) == len(m_b[0])):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    length = len(m_a)
    m = len(m_b[0])
    n = len(m_b)
    m_c = []
    for i in range(length):
        m_c.append([])
        for j in range(m):
            m_c[i].append(0)
            for k in range(n):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return m_c
