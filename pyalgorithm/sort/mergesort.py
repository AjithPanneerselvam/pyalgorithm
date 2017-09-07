"""
    mergesort
    ~~~~~~~~~~~~~~

    Time complexity:
        - Best: O(nlogn)
        - Average: O(nlogn)
        - Worst: O(nlogn)

    Space complexity: O(n)

    Stability: Yes

    Divide and conquer algorithm.

    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from collections import deque


def sort(seq=None):
    if seq is None or len(seq) <= 1:
        return seq

    middle = len(seq) // 2
    left = sort(seq[:middle])
    right = sort(seq[middle:])
    return _merge(left, right)


def _merge(left, right):
    merged, left, right = deque(), deque(left), deque(right)

    while left and right:
        # `deque.pop`: time complexity O(1)
        merged.append(left.popleft() if left[0] < right[0] else right.popleft())

    merged.extend(left if left else right)
    return list(merged)


if __name__ == '__main__':
    print(sort([9, 1, 2, 3]))
