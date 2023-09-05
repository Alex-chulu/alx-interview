#!/usr/bin/python3

"""
makeChange - Determine the fewest number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given amount total.

    Args:
    - coins: A list of coin values.
    - total: The total amount to make change for.

    Returns:
    - The fewest number of coins needed to meet the total.
    - If total is 0 or less, return 0.
    - If total cannot be met by any number of coins you have, return -1.
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
