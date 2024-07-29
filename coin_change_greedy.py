#!/usr/bin/python3
def minimum_coins_greedy(coins, total):
    """
    Calculate the minimum number of coins required to make up a given
    total using a greedy approach.

    Args:
        coins (list[int]): List of coin denominations available.
        total (int): The total amount to be made with the coins.

    Returns:
        int: The minimum number of coins required to make the total using a
        greedy approach. Returns -1 if it's not possible.

    Example:
        >>> minimum_coins_greedy([1, 2, 5], 11)
        3
        >>> minimum_coins_greedy([2], 3)
        -1
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    count = 0
    remaining_total = total

    for coin in coins:
        if remaining_total == 0:
            break
        # Use as many of this coin as possible
        num_coins = remaining_total // coin
        count += num_coins
        remaining_total -= num_coins * coin

    # If we cannot meet the total, return -1
    if remaining_total > 0:
        return -1
    return count
