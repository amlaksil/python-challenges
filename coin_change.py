#!/usr/bin/python3

def minimum_coins_dp(coins, total):
    """
    Calculate the minimum number of coins required to make up a given total
    using dynamic programming.

    Args:
        coins (list[int]): List of coin denominations available.
        total (int): The total amount to be made with the coins.

    Returns:
        int: The minimum number of coins required to make the total.
        Returns -1 if it's not possible.

    Example:
        >>> minimum_coins_dp([1, 2, 5], 11)
        3
        >>> minimum_coins_dp([2], 3)
        -1
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
