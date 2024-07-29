#!/usr/bin/python3
import pytest
from check_duplicate import check_no_duplicate_chars


@pytest.mark.parametrize("text, expected", [
    ('Otto', False),     # 'O' and 'T' are duplicated
    ('Python', True),    # No duplicates
    ('', True),          # Empty string has no duplicates
    ('Aa', False),       # 'A' is duplicated (case-insensitive)
    ('abcdef', True),    # No duplicates
    ('aabbcc', False),  # Duplicates present
    ('12345', True),     # No duplicates
    ('1a2b3c4d5e', True)  # No duplicates
])
def test_check_no_duplicate_chars(text, expected):
    """
    Test the check_no_duplicate_chars function using parameterized
    test cases.

    Args:
        text (str): The input string to check for duplicates.
        expected (bool): Expected result, True if no
        duplicates, False otherwise.

    Asserts:
        The result of check_no_duplicate_chars should match the
        expected result.
    """
    assert check_no_duplicate_chars(text) == expected
