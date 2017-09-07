"""
    quicksort
    ~~~~~~~~~~~~~~

    Time complexity:
        - Best: O(nlogn)
        - Average: O(nlogn)
        - Worst: O(n^2)

    Space complexity:
        - Average: O(nlogn)
        - Worst: O(n)

    Stability: No
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from random import randrange


def sort(seq=None):
    if seq is None:
        return None

    if len(seq) < 2:
        return seq

    _quicksort(seq, 0, len(seq) - 1)
    return seq


def _quicksort(seq, left, right):
    if left < right:
        pivot_index = _partition(seq, left, right)
        _quicksort(seq, left, pivot_index - 1)
        _quicksort(seq, pivot_index + 1, right)


def _partition(seq, left, right):
    pivot_index = randrange(left, right)
    pivot = seq[pivot_index]
    # swap pivot and the right element (temporally)
    seq[pivot_index], seq[right] = seq[right], seq[pivot_index]
    store_index = left

    for i in range(left, right):
        if seq[i] < pivot:
            seq[i], seq[store_index] = seq[store_index], seq[i]
            store_index += 1

    # swap pivot and the stored element
    seq[store_index], seq[right] = seq[right], seq[store_index]
    return store_index


if __name__ == '__main__':
    print(sort([4, 3, 2, 1]))
