#!/usr/bin/python3
import sys

matrix_mul = __import__('100-matrix_mul').matrix_mul

def capture_output(code):
    try:
        output = eval(code)
    except Exception as e:
        output = e
    return output

def main():
    code_snippets = [
        "print(matrix_mul(14, -4))",
        "print(matrix_mul('Matrix1', 'Matrix2'))",
        "print(matrix_mul([[14, -4]], [5, 3]))",
        "print(matrix_mul([14, -4], [5, 3]))",
        "print(matrix_mul([[2, 3]],[]))",
        "print(matrix_mul([],[]))",
        "print(matrix_mul([[2, 3]],[[]]))",
        "print(matrix_mul([[]],[[]]))",
        "print(matrix_mul([[2, 1]], [['str', 18, '1bc6']]))",
        "print(matrix_mul([['str', 18, '1bc6']], [[2, 1]]))",
        "print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4, -7.5]]))",
        "print(matrix_mul([[1, 2], [3, 4, -2]], [[1, 2], [3, 4, -7.5]]))",
        "print(matrix_mul([[1, 2], [3, 4]], [[1, 2, 5], [3, 4, -7.5], [1, 12, -7]]))",
        "print(matrix_mul([[1, 2, 4.2], [3, 4, 0]], [[1, 2], [3, 4]]))",
        "print(matrix_mul([[0, 0]], [[0, 0], [0, 0]]))",
        "print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))",
        "print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))",
        "print(matrix_mul([[11, 3], [7, 11]], [[8, 0, 1], [0, 3, 5]]))",
        "print(matrix_mul([[2, 1], [7, -1], [6, 3], [4, 8]], [[4, 1, 0, -2, 3], [9, -1, 6, 5, 2]]))",
        "print(matrix_mul([[2, 1, 8, 2], [7, -1, 4, 0]], [[4, 1, 0], [9, -1, 6], [4, -10, 2], [8, 0, 0]]))",
        "print(matrix_mul([[2.23, 1.18], [-2.76, 15.0023]], [[-0.04, 1.65, 9.02], [2.075, 6.742, 4.6]]))",
    ]

    with open("output.txt", "w") as f:
        for code in code_snippets:
            f.write(">>>{}\n".format(code))
            f.write("{}\n".format(capture_output(code)))
            f.write("\n")

if __name__ == "__main__":
    main()
