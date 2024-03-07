#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """Create Pascal triangle"""
    if n <= 0:
        return []

    pascal_triangle = [[1]]

    for row_num in range(1, n):
        new_row = [1]
        previous_row = pascal_triangle[row_num - 1]

        for col_num in range(1, row_num):
            new_row.append(previous_row[col_num - 1] + previous_row[col_num])

        new_row.append(1)
        pascal_triangle.append(new_row)

    return pascal_triangle
