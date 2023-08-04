#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N):
    def backtrack(row):
        if row == N:
            solutions.append(list(board))
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)

    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    backtrack(0)

    for solution in solutions:
        print("[", end="")
        for i in range(N):
            print("[{}, {}]".format(i, solution[i]), end="")
            if i != N - 1:
                print(", ", end="")
        print("]")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)

