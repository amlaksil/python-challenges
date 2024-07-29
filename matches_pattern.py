#!/usr/bin/python3

def matches_pattern(pattern, text):
    """
    Check if the given text matches the pattern, where each
    unique character in the pattern corresponds to a unique
    word in the text.

    Args:
        pattern (str): A string where each character is a placeholder.
        text (str): A string of words to match against the pattern.

    Returns:
        bool: True if the text matches the pattern, False otherwise.

    Example:
        >>> matches_pattern('xyyx', 'tim mike mike tim')
        True
        >>> matches_pattern('xyyx', 'time mike tom tim')
        False
    """
    values = text.split()
    if len(values) != len(pattern):
        return False

    placeholder_to_value_map = {}

    for i, pattern_char in enumerate(pattern):
        value = values[i]
        if pattern_char not in placeholder_to_value_map:
            if value in placeholder_to_value_map.values():
                return False  # One value cannot map to multiple placeholders
            placeholder_to_value_map[pattern_char] = value
        else:
            if placeholder_to_value_map[pattern_char] != value:
                return False

    return True
