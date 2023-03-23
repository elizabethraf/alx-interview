#!/usr/bin/python3
"""Display Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal triangle"""
    if n <= 0:
        tree = [[]]
    else:
        tree = [[1]]
        for a in range(n - 1):
            prev = [0] + tree[-1] + [0]
            newlist = []
            for b in range(len(tree[-1]) + 1):
                newlist.append(prev[b] + prev[b + 1])
            tree.append(newlist)
    return tree
