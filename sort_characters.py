#!/usr/bin/python3
def sort_characters_by_frequency(chars):
    """
    Sorts characters in the input string by frequency and
    returns them in order.
    Args:
        chars (str): The input string containing uppercase alphabetical chars

    Return:
        str: A string where characters are sorted by frequency
    """
    freq = [0] * 91  # Frequency array for characters 'A' to 'Z'

    # Count frequency of each character in the input string
    for char in chars:
        freq[ord(char)] += 1

    result = ''
    for i in range(65, 91):  # Iterates through ASCII values for 'A' to 'Z'
        if freq[i] != 0:
            result += freq[i] * chr(i)

    return result


if __name__ == '__main__':
    chars = "ABACCBBCAACCBBA"
    sorted_characters = sort_characters_by_frequency(chars)
    print(sorted_characters)
