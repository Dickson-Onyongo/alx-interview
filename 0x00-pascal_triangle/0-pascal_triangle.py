#!/usr/bin/python3
"""
A script to determine the Pascals Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of intergers representing the Pascals Triangle of n.
    """
    list = []
    if n <= 0:
        return list

    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(list[i-1][j-1] + list[i-1][j])
        list.append(temp_list)
    #print list(the triangle)
    return list
