#!/usr/bin/python3
"""Module of matrix multiplication
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices
        with the help of numpy
    """
    return np.matmul(m_a, m_b)