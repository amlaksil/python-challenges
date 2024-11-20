#!/usr/bin/python3
import pytest
from sort_characters import sort_characters_by_frequency


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("ABAABBBAAABBBA", "AAAAAAABBBBBBB"),
        ("ABACCBBCAACCBBA", "AAAAABBBBBCCCCC"),
        ("AAA", "AAA"),
        ("", ""),
        ("A", "A"),
        ("ZZZZY", "YZZZZ")
    ]
)
def test_sort_characters_by_frequency(input_string, expected_output):
    assert sort_characters_by_frequency(input_string) == expected_output
