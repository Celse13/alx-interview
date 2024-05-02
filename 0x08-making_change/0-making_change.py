#!/usr/bin/python3
""" challenge module """


def makeChange(coins, total):
    '''Return the minimum number of coins needed to
        make change for the total
    '''
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[total] if dp[total] <= total else -1
