#!/usr/bin/python3
import pytest
from binary_search import binary_search


@pytest.mark.parametrize(
    "input_values, search_for, expected_result",
    [
        ([1, 2, 3, 4, 5, 7, 8, 9], 5, True),
        ([1, 2, 3, 4, 5, 7, 8, 9], 6, False),
        ([1, 2, 3, 4, 5], 3, True),
        ([10, 20, 30, 40], 10, True),
        ([10, 20, 30, 40], 40, True),
        ([1, 3, 5, 7, 9], 2, False),
        ([1], 1, True),
        ([], 1, False)
    ]
)
def test_binary_search(input_values, search_for, expected_result):
    result = binary_search(input_values, search_for)
    assert result == expected_result
