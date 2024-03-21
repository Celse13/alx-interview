#!/usr/bin/python3
"""Operations"""


def minOperations(n):
    """Operations"""
    if n <= 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return i + minOperations(n // i)
    return n
