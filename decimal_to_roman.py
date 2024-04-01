#!/usr/bin/python3
"""
This module provides a function to convert a decimal value to a Roman numeral
representation.
"""


def to_roman_number(value):
    """
    Converts a decimal number to a Roman numeral representation.

    Args:
        value (int): The decimal number to be converted.

    Returns:
        str: The Roman numeral representation of the input decimal number.
    """
    decimal_roman = [
            (1000, 'M'), (900, 'CM'), (500, 'D'),
            (400, 'CD'), (100, 'C'), (90, 'XC'),
            (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
            ]
    roman = ""
    for digit, symbol in decimal_roman:
        while value >= digit:
            roman += symbol
            value -= digit
    return roman


if __name__ == '__main__':
    print(to_roman_number(489))
