#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [True for _ in range(max(n + 1, 2))]
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    primes = [i for i, p in enumerate(primes) if p]
    wins = 0
    for n in nums:
        wins += sum(p <= n for p in primes) % 2 == 1
    return "Maria" if wins * 2 == len(nums) else "Ben"
