#!/usr/bin/python3
import pytest
from matches_pattern import matches_pattern
import pytest


@pytest.mark.parametrize(
    "pattern, text, expected",
    [("x", "", False),
     ("", "x", False),
     ("xyyx", "tim mike mike tim", True),
     ("xyyx", "time mike tom tim", False),
     ("xyxx", "tim mike mike tim", False),
     ("xxxx", "tim tim tim tim", True),
     ("", "", True),  # Both pattern and text are empty
     ("x", "a", True),  # Single character pattern and single word text
     ("x", "a a", False),  # Single character pattern but multiple words
     ("xxy", "a a a", False)])  # Single pattern but multiple words
def test_matches_pattern(pattern, text, expected):
    """
    Test the matches_pattern function using parameterized test cases.

    Args:
        pattern (str): The pattern to check.
        text (str): The text to match against the pattern.
        expected (bool): Expected result, True if the text matches
        the pattern, False otherwise.

    Asserts:
        The result of matches_pattern should match the expected result.
    """
    assert matches_pattern(pattern, text) == expected
