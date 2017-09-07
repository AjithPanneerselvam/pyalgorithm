"""
    insertionsort
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

    for i in range(1, len(seq)):
        value = seq[i]

        j = i
        while j > 0 and seq[j - 1] > value:
            seq[j] = seq[j - 1]
            j -= 1

        seq[j] = value

    return seq


if __name__ == '__main__':
    print(sort([3, 8, 2, 1, 9]))
