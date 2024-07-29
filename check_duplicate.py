#!/usr/bin/python3
def check_no_duplicate_chars(text):
    """
    Check if a given string contains no duplicate characters, case-insensitive.

    Args:
        text (str): The input string to check for duplicate characters.

    Returns:
        bool: True if there are no duplicate characters in the
        string, False otherwise.

    Example:
        >>> check_no_duplicate_chars('Otto')
        False
        >>> check_no_duplicate_chars('Python')
        True
        >>> check_no_duplicate_chars('')
        True
        >>> check_no_duplicate_chars('Aa')
        False
    """
    contained_chars = set()

    for current_char in text.upper():
        if current_char in contained_chars:
            return False
        contained_chars.add(current_char)
    return True


if __name__ == '__main__':
    print(check_no_duplicate_chars('Otto'))
