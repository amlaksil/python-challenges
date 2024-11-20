#!/usr/bin/python3
def binary_search_iterative(values, search_for):
    """
    Performs an iterative binary search to find the
    index of a value in a sorted list.

    Args:
        values (list): A sorted list of values.
        search_for (int/float): The value to search for in the list.

    Returns:
        int: The index of the value if found, otherwise -1.
    """
    left = 0
    right = len(values) - 1

    while right >= left:
        mid_idx = (left + right) // 2

        if search_for == values[mid_idx]:
            return mid_idx

        if search_for < values[mid_idx]:
            right = mid_idx - 1
        else:
            left = mid_idx + 1
    return -1


if __name__ == '__main__':
    print(binary_search_iterative([1, 2, 3, 4, 5, 7, 8, 9], 6))
