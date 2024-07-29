#!/usr/bin/python3

def check_parentheses(braces_input):
    """
    Check if the given string of braces is balanced.

    Args:
        braces_input (str): The input string containing braces
        (parentheses, brackets, and curly braces).

    Returns:
        bool: True if the braces are balanced, False otherwise.

    Example:
        >>> check_parentheses("()")
        True
    """
    stack = []
    parentheses = {'(': ')', '[': ']', '{': '}'}

    for brace in braces_input:
        if brace in parentheses:
            stack.append(brace)
        elif stack and brace == parentheses[stack[-1]]:
            stack.pop()
        else:
            return False

    return not stack
