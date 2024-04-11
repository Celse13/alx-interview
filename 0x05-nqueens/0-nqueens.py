#!/usr/bin/python3
"""N queens"""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for q in range(col):
        if board[q] == row or \
                board[q] - q == row - col or \
                board[q] + q == row + col:
            return False
    return True


def nqueens(size):
    def solve_NQueen(board, col):
        """Solve N queens"""
        j = len(board)
        if col == j:
            print(str([[q, board[q]] for q in range(j)]))
            return
        for row in range(j):
            if is_safe(board, row, col):
                board[col] = row
                solve_NQueen(board, col + 1)

    brd = [-1 for _ in range(size)]
    solve_NQueen(brd, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    n = sys.argv[1]
    if not n.isdigit():
        print("N must be a number")
        exit(1)
    if int(n) < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(int(n))
