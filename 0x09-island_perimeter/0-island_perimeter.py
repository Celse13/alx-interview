#!/usr/bin/python3
"""Calculate perimenter module"""


def island_perimeter(grid):
    """ calculate perimeter """
    pm = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                pm += 4
                if i > 0 and grid[i - 1][j] == 1:
                    pm -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    pm -= 2
    return pm
