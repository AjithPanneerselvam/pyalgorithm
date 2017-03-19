"""
    Lowest Common Multiple
"""


def lcm(a, b):
    tmp_a = max(a,b)
    tmp_b = min(a,b)
    while (tmp_a % tmp_b) != 0:
        tmp_a += tmp
    return tmp_a
