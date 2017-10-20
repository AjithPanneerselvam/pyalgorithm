"""
    selectionsort
    ~~~~~~~~~~~~~~

    Time complexity:
        - Best: O(n^2)
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

    for i in range(0, len(seq)):
        min_index = i
        for j in range(i + 1, len(seq)):
            if seq[j] < seq[min_index]:
                min_index = j

        seq[min_index], seq[i] = seq[i], seq[min_index]

    return seq


if __name__ == '__main__':
    print(sort([1, 2, 3, 1, 0]))
