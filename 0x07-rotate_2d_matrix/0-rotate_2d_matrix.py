#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    """

    # Get the size of the matrix
    n = len(matrix)

    # Transpose the matrix (swap elements across the main diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
