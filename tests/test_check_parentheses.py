#!/usr/bin/python3
import pytest
from check_parentheses import check_parentheses


@pytest.mark.parametrize(
    "braces_input, expected",
    [
        ("()", True),                 # Simple balanced parentheses
        ("{[()()]}", True),           # Complex balanced braces
        ("((()))", True),             # Nested balanced parentheses
        ("({[)]}", False),            # Mismatched braces
        ("(((", False),               # Unbalanced parentheses
        ("", True),                   # Empty string is balanced
        ("[{()]}", False),            # Balanced with mixed braces
        ("]", False),                 # Unbalanced with extra closing brace
        ("[(", False),                # Unbalanced with unmatched opening brace
    ]
)
def test_check_parentheses(braces_input, expected):
    """
    Test the check_parentheses function using parameterized test cases.

    Args:
        braces_input (str): The input string containing braces.
        expected (bool): Expected result, True if braces are
        balanced, False otherwise.

    Asserts:
        The result of check_parentheses should match the expected result.
    """
    assert check_parentheses(braces_input) == expected
