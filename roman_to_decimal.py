#!/usr/bin/python3
"""
This module provides a function to convert a Roman numeral to decimal
value representation.
"""


def from_roman_number(roman_number):
    """
    Converts a Roman numeral to its corresponding decimal value.

    Args:
        roman_number (str): The Roman numeral string to be converted.

    Returns:
        int: The decimal value of the Roman numeral.

    Raises:
        None

    Example:
        >>> from_roman_number("MMMCMXCIX")
        3999
    """
    roman_decimal = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    subtractives = {
        "IV": 4, "IX": 9, "XL": 40,
        "XC": 90, "CD": 400, "CM": 900}
    sum = i = 0
    while i < len(roman_number):
        if i != len(roman_number) - 1:
            chars = roman_number[i:i+2]
        if chars in subtractives:
            sum += subtractives[chars]
            i += 1
        else:
            sum += roman_decimal[roman_number[i]]
        i += 1
    return sum


if __name__ == '__main__':
    print(from_roman_number("MMMCMXCIX"))
