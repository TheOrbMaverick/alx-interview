#!/usr/bin/python3
"""
Determine the fewest amount of coins required
"""

def makeChange(coins, total):
    if (total <= 0):
        return 0
    
    # List of min coins required
    dp = [float('inf')] * (total + 1)
    # Base case: 0 coins needed to meet a total of 0
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else - 1
