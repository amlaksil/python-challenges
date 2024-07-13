#!/usr/bin/python3
import pytest


def generate_parenthesis(n):
    """
    Generate all valid combinations of n pairs of parentheses.

    Args:
    - n (int): Number of pairs of parentheses to generate.

    Returns:
    - list: A list of strings representing valid combinations of parentheses.

    Examples:
    >>> generate_parenthesis(3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']

    >>> generate_parenthesis(1)
    ['()']

    >>> generate_parenthesis(0)
    ['']
    """
    results = []

    # Use a list to simulate queue, each item is
    # (current_string, open_count, close_count)
    queue = [("", 0, 0)]

    front = 0  # pointer to the front of the queue

    while front < len(queue):
        current, open_count, close_count = queue[front]
        front += 1

        # If we've used all n pairs of parentheses, add current to results
        if open_count == n and close_count == n:
            results.append(current)

        # Add '(' if we haven't used up all n open parentheses yet
        if open_count < n:
            queue.append((current + '(', open_count + 1, close_count))

        # Add ')' if it doesn't exceed the number of '(' added
        if close_count < open_count:
            queue.append((current + ')', open_count, close_count + 1))

    return results


@pytest.mark.parametrize("n, expected", [
    (0, ['']),
    (1, ['()']),
    (2, ['(())', '()()']),
    (3, ['((()))', '(()())', '(())()', '()(())', '()()()']),
    (4, ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))',
         '(()()())', '(()())()', '(())(())', '(())()()', '()((()))',
         '()(()())', '()(())()', '()()(())', '()()()()']),
])
def test_generate_parenthesis(n, expected):
    assert generate_parenthesis(n) == expected


if __name__ == '__main__':
    pytest.main()
