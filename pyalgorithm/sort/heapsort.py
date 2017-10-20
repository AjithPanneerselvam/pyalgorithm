"""
    heapsort
    ~~~~~~~~~~~~~~

    Time complexity:
        - Best: O(nlogn)
        - Average: O(nlogn)
        - Worst: O(nlogn)

    Space complexity: O(1)

    Stability: No
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def sort(seq=None):
    if seq is None or len(seq) <= 1:
        return seq

    length = len(seq)
    seq = _build_heap(seq, length)

    for i in range(length - 1, 0, -1):
        # swap the largest element with the last one
        seq[i], seq[0] = seq[0], seq[i]
        _heapify(seq, 0, i)

    return seq


def _build_heap(seq, length):
    for n in range(length // 2, -1, -1):
        _heapify(seq, n, length)

    return seq


def _heapify(seq, index, length):
    max_index = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < length and seq[left] > seq[max_index]:
        max_index = left

    if right < length and seq[right] > seq[max_index]:
        max_index = right

    if max_index != index:
        seq[index], seq[max_index] = seq[max_index], seq[index]
        _heapify(seq, max_index, length)


if __name__ == '__main__':
    print(sort([1, 3, 8, 2]))
