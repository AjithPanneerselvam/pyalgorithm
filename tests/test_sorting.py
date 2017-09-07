"""
    test_sorting
    ~~~~~~~~~~~~~~

    Tests for sorting algorithms
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from pyalgorithm.sort import (bubble_sort, heap_sort, insertion_sort,
                              merge_sort, quick_sort, quick_sort_inplace,
                              selection_sort, shell_sort)


@pytest.fixture(params=[bubble_sort, heap_sort, insertion_sort,
                        merge_sort, quick_sort, quick_sort_inplace,
                        selection_sort, shell_sort])
def sort_func(request):
    return request.param


@pytest.mark.parametrize('seq, out',
                         [
                             (None, None),
                             ([], []),
                             ([1], [1]),
                         ])
def test_sort_with_boundary_seq(sort_func, seq, out):
    ret = sort_func(seq)
    if ret:
        assert ret == out


@pytest.mark.parametrize('seq, out',
                         [
                             ([1, 2], [1, 2]),
                             ([2, 1], [1, 2]),
                             ([2, 1, 1, 2], [1, 1, 2, 2]),
                             ([2, 1, 3, 5], [1, 2, 3, 5]),
                         ])
def test_sort_with_normal_seq(sort_func, seq, out):
    assert sort_func(seq) == out
