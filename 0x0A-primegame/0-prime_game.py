#!/usr/bin/python3
"""checks who wins the game"""


def isWinner(r, ns):
    """Check who wins the game"""
    if not ns or r < 1:
        return None

    m = max(ns)
    ps = [True for _ in range(max(m + 1, 2))]
    ps[0] = ps[1] = False
    for i in range(2, int(m ** 0.5) + 1):
        if ps[i]:
            for j in range(i * i, m + 1, i):
                ps[j] = False

    pc = [0] * (m + 1)
    for i in range(1, m + 1):
        pc[i] = pc[i - 1] + ps[i]

    mw = 0
    bw = 0

    for n in ns:
        if pc[n] % 2 == 0:
            bw += 1
        else:
            mw += 1

    if mw == bw:
        return None

    return "Maria" if mw > bw else "Ben"
