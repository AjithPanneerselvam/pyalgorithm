# -*-coding: utf-8-*-


def search(seq, key):
    """Implementation of interpolation search algorithm.
    See `https://en.wikipedia.org/wiki/Interpolation_search` for details.

    :param seq: a list of items
    :param key: target to be searched for
    :return: the index of where the `key` is located in the list. If `key` is
            not found then Node is returned.
    """
    if seq is None:
        return None

    high, low = len(seq) - 1, 0

    while low < high:
        mid = low + (key - seq[low]) * (high - low) // (seq[high] - seq[low])
        if seq[mid] > key:
            high = mid - 1
        elif seq[mid] < key:
            low = mid + 1
        else:
            return mid
    else:
        return low if key == seq[low] else None


if __name__ == '__main__':
    s = [1, 2, 4, 7, 9, 10]
    assert 0 == search(s, 1)
    assert 3 == search(s, 7)
    assert 5 == search(s, 10)
    assert search(s, 0) is None
