#!/usr/bin/python3
"""
Determine the fewest number of coins required to meet a given total.
"""


def makeChange(coins, total):
    # Edge case where total is zero or negative
    if total <= 0:
        return 0

    # Sort coins to improve efficiency with early exits
    coins.sort()

    # Initialize dp array to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make a total of 0

    # Loop through each coin and update the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            # Update dp[i] only if the current coin is smaller or equal to i
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return -1 if no solution was found; otherwise return dp[total]
    return dp[total] if dp[total] != float('inf') else -1
