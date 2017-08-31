""" Linear search
Time complexity - O(n)
"""


def linear_search(ls, val):
    for i in range(len(ls)):
        if ls[i] == val:
            # Found! Returns the index
            return i + 1
    # Not found
    return None
