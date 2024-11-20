#!/usr/bin/python3

def binary_search(values, search_for):
    """
    Perform binary search on a sorted list to check if a value exists.

    Args:
        values (list): A sorted list of values (must be sorted).
        search_for (int/float): The value to search for in the list.

    Returns:
        bool: True if the value is found, False otherwise.
    """
    return binary_search_in_range(values, search_for, 0, len(values) - 1)


def binary_search_in_range(values, search_for, left, right):
    """
    Helper function that performs binary search in a specific
    range of the list.

    Args:
        values (list): A sorted list of values.
        search_for (int/float): The value to search for.
        left (int): The starting index of the range.
        right (int): The ending index of the range.

    Returns:
        bool: True if the value is found, False otherwise.
    """
    if right >= left:
        mid_idx = (left + right) // 2

        if search_for == values[mid_idx]:
            return True

        if search_for < values[mid_idx]:
            return binary_search_in_range(
                values,
                search_for,
                left,
                mid_idx - 1
            )
        else:
            return binary_search_in_range(
                values,
                search_for,
                mid_idx + 1,
                right
            )
    return False


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5, 7, 8, 9], 5))  # Expected output: True
    print(binary_search([1, 2, 3, 4, 5, 7, 8, 9], 6))  # Expected output: False
