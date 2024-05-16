#!/usr/bin/python3
"""checks who wins the game"""


def isWinner(x, nums):
    """checks who wins the game"""
    def generate_primes(n):
        primes = [True for _ in range(n+1)]
        p = 2
        while p * p <= n:
            if primes[p] == True:
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1
        return primes

    Maria_wins = 0
    Ben_wins = 0

    for n in nums:
        primes = generate_primes(n)
        prime_count = sum(primes) - 2
        if prime_count % 2 == 0:
            Ben_wins += 1
        else:
            Maria_wins += 1

    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    else:
        return None
