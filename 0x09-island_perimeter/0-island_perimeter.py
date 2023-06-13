#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Display Island Perimeter"""
    if not grid:
        return 0

    perimeter = 0
    for rows in range(len(grid)):
        for cols in range(len(grid[rows])):
            if grid[rows][cols] == 1:
                if rows == 0 or grid[rows - 1][cols] == 0:
                    perimeter += 1
                if cols == 0 or grid[rows][cols - 1] == 0:
                    perimeter += 1
                if rows == len(grid) - 1 or grid[rows + 1][cols] == 0:
                    perimeter += 1
                if cols == len(grid[rows]) - 1 or grid[rows][cols + 1] == 0:
                    perimeter += 1
    return perimeter
