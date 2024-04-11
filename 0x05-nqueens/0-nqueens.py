#!/usr/bin/env python3
import sys


def safe(b, r, c):
    """Check if a queen can be placed at row r and column c
        without attacking any other queen
    """
    for q in range(c):
        if b[q] == r or b[q] - q == r - c or b[q] + q == r + c:
            return False
    return True


def solve(b, c):
    """Solve the n-queens problem using backtracking"""
    s = len(b)
    if c == s:
        print(str([[q, b[q]] for q in range(s)]))
        return
    for r in range(s):
        if safe(b, r, c):
            b[c] = r
            solve(b, c + 1)


def queens(n):
    b = [-1 for _ in range(n)]
    solve(b, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = sys.argv[1]
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(n) < 4:
        print("N must be at least 4")
        sys.exit(1)
    queens(int(n))
