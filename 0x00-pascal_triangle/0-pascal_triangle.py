#!/usr/bin/python3
"""Pascal Triangle Interview new Challenge"""


def pascal_triangle(n):
    """matrix pascale triangle"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        # starts and ends with zero
        next_row = [0] * (i+1)
        next_row[0] = 1
        next_row[len(next_row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(next_row):
                a = pascal_triangle[i - 1][j]
                b = pascal_triangle[i - 1][j - 1]
                next_row[j] = a + b

        pascal_triangle[i] = next_row

    return pascal_triangle
