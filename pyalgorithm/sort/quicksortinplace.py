"""
    quicksort_inplace
    ~~~~~~~~~~~~~~

    Time complexity:
        - Best: O(nlogn)
        - Average: O(nlogn)
        - Worst: O(n^2)

    Space complexity: O(n^2)

    Stability: No
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def sort(seq=None):
    if not seq:
        return seq

    pivot = seq[0]
    left = [element for element in seq[1:] if element < pivot]
    right = [element for element in seq[1:] if element >= pivot]
    return sort(left) + [pivot] + sort(right)


if __name__ == '__main__':
    print(sort([3, 2, 1, 0, 1]))
