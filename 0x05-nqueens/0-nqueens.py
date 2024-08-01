#!/usr/bin/python3
""" The N Qoueens problem """
import sys


def is_safe(board, row, col, N):
    """ Check if it is safe to place queen """
    # Check the column
    for i in range(row):
        if board[i] == col:
            return False

    # Check for diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_queens(N):
    """ Solution to queens problem """
    def solve(board, row):
        if row == N:
            solution = []
            for i in range(N):
                solution.append([i, board[i]])
            solutions.append(solution)
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1
    solutions = []
    board = [-1] * N
    solve(board, 0)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_queens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
