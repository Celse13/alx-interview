#!/usr/bin/python3
"""checks who wins the game"""


def isWinner(rounds, numbers):
    """Prime Game"""
    if not numbers or rounds < 1:
        return None
    max_num = max(numbers)
    prime_flags = [True for _ in range(max(max_num + 1, 2))]
    prime_flags[0] = prime_flags[1] = False
    for index in range(2, int(max_num ** 0.5) + 1):
        if prime_flags[index]:
            for j in range(index * index, max_num + 1, index):
                prime_flags[j] = False
    prime_numbers = [i for i, is_prime in enumerate(prime_flags) if is_prime]
    victories = 0
    for num in numbers:
        victories += sum(prime <= num for prime in prime_numbers) % 2 == 1
    return "Maria" if victories * 2 == len(numbers) else "Ben"
