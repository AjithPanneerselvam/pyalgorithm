"""
    shellsort
    ~~~~~~~~~~~~~~

    Time complexity:
        - Worst: O(n^2)

    Space complexity: O(1)

    Stability: No
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def sort(seq=None):
    if seq is None or len(seq) <= 1:
        return seq

    length = len(seq)
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            # insertion sort algorithm
            value = seq[i]
            j = i
            while j >= gap and seq[j - gap] > value:
                seq[j] = seq[j - gap]
                j -= gap
            seq[j] = value
        gap //= 2

    return seq


if __name__ == '__main__':
    print(sort([2, 1, 7]))
