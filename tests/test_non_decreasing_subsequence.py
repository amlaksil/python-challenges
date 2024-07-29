#!/usr/bin/python3
import pytest
from non_decreasing_subsequence import longest_non_decreasing_subsequence


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 1, 3, 2, 3, 4], [2, 3, 4]),   # General case
        ([5, 3, 4, 7], [3, 4, 7]),  # Non-decreasing subsequence with gaps
        ([9, 8, 7, 6], [9]),                      # Decreasing sequence
        ([1], [1]),                              # Single element
        ([], []),                                # Empty list
        ([1, 2, 2, 3, 1, 4, 5], [1, 2, 2, 3]),  # Subsequence with duplicates
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [5]),             # Strictly decreasing sequence
    ]
)
def test_longest_non_decreasing_subsequence(values, expected):
    """
    Test the longest_non_decreasing_subsequence function using
    parameterized test cases.

    Args:
        values (list[int]): The list of integers to test.
        expected (list[int]): The expected longest non-decreasing subsequence.

    Asserts:
        The result of longest_non_decreasing_subsequence should
        match the expected result.
    """
    assert longest_non_decreasing_subsequence(values) == expected
