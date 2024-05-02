#!/usr/bin/python3
""" challenge module """


def makeChange(coins, total):
    """ makeChange"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    number_of_coins = 0
    for _coin in coins:
        if total <= 0:
            break
        number_of_coins += total // _coin
        total %= _coin

    if total != 0:
        return -1
    return number_of_coins
