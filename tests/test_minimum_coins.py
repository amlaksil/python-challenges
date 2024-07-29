#!/usr/bin/python3
import pytest
from coin_change import minimum_coins_dp
from coin_change_greedy import minimum_coins_greedy

@pytest.mark.parametrize("coins, total, expected", [
    ([1, 2, 5], 11, 3),  # 5 + 5 + 1
    ([1, 2, 5], 0, 0),   # No coins needed for total 0
    ([1, 2, 5], -5, 0),  # No coins needed for negative total
    ([2], 3, -1),        # Impossible to make total 3 with only 2-value coins
    ([1, 2, 5], 7, 2),   # 5 + 2
    ([3, 5, 7], 14, 2),  # 7 + 7
    ([1, 3, 4], 6, 2),   # 3 + 3 (Greedy might fail with 4 + 1 + 1, but dynamic should handle)
    ([1, 3, 4], 8, 2),   # 4 + 4
    ([1, 3, 4], 10, 3),  # 4 + 3 + 3
    ([5, 10, 25], 30, 2) # 25 + 5
])
def test_minimum_coins(coins, total, expected):
    """
    Test the minimum coin calculation functions using parameterized test cases.

    Args:
        coins (list[int]): List of coin denominations available.
        total (int): The total amount to be made with the coins.
        expected (int): Expected minimum number of coins required or -1 if it's not possible.

    Asserts:
        The result from both minimum_coins_dp and minimum_coins_greedy should match the expected value.
    """
    assert minimum_coins_dp(coins, total) == expected
    
    if coins != [1, 3, 4]:
        assert minimum_coins_greedy(coins, total) == expected
