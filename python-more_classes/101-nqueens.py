#!/usr/bin/python3
"""
Solves the N-queens puzzle
"""
import sys


def nqueens():
    """Main function to solve N-queens"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = []

    def solve(row):
        """Backtracking logic to find solutions"""
        if row == n:
            print(solutions)
            return

        for col in range(n):
            safe = True
            for r, c in solutions:
                if c == col or abs(r - row) == abs(c - col):
                    safe = False
                    break
            if safe:
                solutions.append([row, col])
                solve(row + 1)
                solutions.pop()

    solve(0)


if __name__ == "__main__":
    nqueens()