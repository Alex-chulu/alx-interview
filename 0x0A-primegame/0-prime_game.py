#!/usr/bin/python3
"""
isWinner - Determine the winner of the game played by Maria and Ben.
"""

def isWinner(x, nums):
    """
    Determine the winner of the game based on given rounds and numbers.

    Args:
    - x: The number of rounds to play.
    - nums: An array of integers representing different values of n for each round.

    Returns:
    - The name of the player who won the most rounds. If there's a tie, return None.
    """
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def play_game(n):
        if n <= 1:
            return "Ben"
        elif n % 2 == 0:
            return "Maria"
        elif is_prime(n):
            return "Maria"
        else:
            return "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
