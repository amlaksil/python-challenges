#!/usr/bin/python3
import pytest
from bsearch_iterative import binary_search_iterative


@pytest.mark.parametrize(
    "input_values, search_for, expected_result",
    [
        ([1, 2, 3, 4, 5, 7, 8, 9], 5, 4),
        ([1, 2, 3, 4, 5, 7, 8, 9], 6, -1),
        ([1, 2, 3, 4, 5], 3, 2),
        ([10, 20, 30, 40], 10, 0),
        ([10, 20, 30, 40], 40, 3),
        ([1, 3, 5, 7, 9], 2, -1),
        ([1], 1, 0),
        ([], 1, -1)
    ]
)
def test_binary_search(input_values, search_for, expected_result):
    result = binary_search_iterative(input_values, search_for)
    assert result == expected_result
