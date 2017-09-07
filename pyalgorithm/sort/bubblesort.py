"""
    bubblesort
    ~~~~~~~~~~~~~~

    Time complexity:
        - Best: O(n)
        - Average: O(n^2)
        - Worst: O(n^2)

    Space complexity: O(1)

    Stability: Yes
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def sort(seq=None):
    if seq is None or len(seq) <= 1:
        return seq

    length = len(seq)
    for i in range(0, length):
        is_swapped = False
        for j in range(length - 1, i, -1):
            if seq[j - 1] > seq[j]:
                is_swapped = True
                seq[j - 1], seq[j] = seq[j], seq[j - 1]

        if not is_swapped:
            return seq

    return seq


if __name__ == '__main__':
    print(sort([3, 4, 1, 10, 20, 7]))
