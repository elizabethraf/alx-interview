#!/usr/bin/python3
"""Display Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal triangle"""
    if n <= 0:
        return []

        list = [[1]]
        for a in range(n - 1):
            newlist = []
            prev = [0] + list[-1] + [0]
            for b in range(len(list)-1):
                newlist.append(prev[b] + prev[b+1])
            list.append(newlist)
        return list
