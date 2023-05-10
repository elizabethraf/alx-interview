#!/usr/bin/python3
"""Display 2D matrix, rotate it 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Display 2D matrix"""
    n = len(matrix)

    for b in range(n):
        for j in range(b, n):
            matrix[b][j], matrix[j][b] = matrix[j][b], matrix[b][j]

    for b in range(n):
        for j in range(n // 2):
            matrix[b][j], matrix[b][n - j - 1] \
                = matrix[b][n - j - 1], matrix[b][j]
