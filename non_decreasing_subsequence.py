#!/usr/bin/python3
def longest_non_decreasing_subsequence(values):
    """
    Find the longest non-decreasing subsequence in a list of values.

    Args:
        values (list[int]): A list of integers.

    Returns:
        list[int]: The longest non-decreasing subsequence.

    Example:
        >>> longest_non_decreasing_subsequence([1, 2, 1, 3, 2, 3, 4])
        [1, 2, 3, 4]
        >>> longest_non_decreasing_subsequence([5, 3, 4, 7])
        [3, 4, 7]
        >>> longest_non_decreasing_subsequence([9, 8, 7, 6])
        [9]
        >>> longest_non_decreasing_subsequence([1])
        [1]
        >>> longest_non_decreasing_subsequence([])
        []
    """
    # Handle edge cases
    if not values:
        return []

    if len(values) == 1:
        return values

    # Initialize variables
    longest = (0, 0)
    start = 0

    # Iterate over the list
    for end in range(1, len(values)):
        if values[end - 1] <= values[end]:
            # Update the longest non-decreasing subsequence indices if needed
            if end - start > longest[1] - longest[0]:
                longest = (start, end)
        else:
            # Update start index for the new subsequence
            start = end

    # Return the longest non-decreasing subsequence
    return values[longest[0]:longest[1] + 1]
