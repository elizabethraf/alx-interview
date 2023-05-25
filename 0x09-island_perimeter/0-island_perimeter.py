#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Display Island Perimeter"""
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    for i in range(rows):
        if grid[i][0] == 1:
            perimeter -= 1
        if grid[i][cols - 1] == 1:
            perimeter -= 1

    for j in range(cols):
        if grid[0][j] == 1:
            perimeter -= 1
        if grid[rows - 1][j] == 1:
            perimeter -= 1

    return perimeter
