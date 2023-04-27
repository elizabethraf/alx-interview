#!/usr/bin/python3
"""Define The N queens puzzle"""
import sys


def nqueens(N):
    """Define nqueens"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_valid(board, row, col):
        """Display is valid"""
        for i in range(row):
            if board[i][1] == col or \
                board[i][1] - board[i][0] == col - row or \
                board[i][1] + board[i][0] == col + row:
                return False
        return True

    def nqueens_helper(board, row):
        """Display helper"""
        if row == N:
            print(board)
            return
        for col in range(N):
            if is_valid(board, row, col):
                board.append([row, col])
                nqueens_helper(board, row+1)
                board.pop()

    nqueens_helper([], 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
