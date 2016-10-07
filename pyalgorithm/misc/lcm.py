"""
    Lowest Common Multiple
"""


def lcm(a, b):
    tmp_a = a
    while (tmp_a % b) != 0:
        tmp_a += a
    return tmp_a
