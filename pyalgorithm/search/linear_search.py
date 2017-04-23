""" Linear search
Time complexity - O(n)
"""

def linear search(ls,val):
    for i in range(len(ls)):
        if ls[i] == val:
            # Found! Returs the index
            return i+1
    #Not found
    return None
